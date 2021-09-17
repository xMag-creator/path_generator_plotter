from PIL import Image, ImagePalette


def load_image(image):
    # Load image then return tuple with pixel matrix and image size.
    with Image.open('25_2.png') as image:
        image_matrix = image.load()
        image_size = image.size

    return image_matrix, image_size


def order_image_by_colors(image_matrix, image_size):
    # order image pixel by color 
    color_palette = []
    paths = []

    color_palette.append(image_matrix[0, 0])
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            unmatched = 0
            for color in color_palette:
                if image_matrix[i, j] != color:
                    unmatched += 1
            if unmatched == len(color_palette):
                color_palette.append(image_matrix[i, j])
                paths.append({
                    'color': image_matrix[i, j],
                    'path': [{'x': i, 'y': j}]
                })
            elif i == 0 and j == 0:
                paths.append({
                    'color': image_matrix[0, 0],
                    'path': [{'x': 0, 'y': 0}]
                })
            else:
                for n in range(len(paths)):
                    if image_matrix[i, j] == paths[n]['color']:
                        paths[n]['path'].append({'x': i, 'y': j})
    
    return paths


def detect_y_stripes(paths):
    # detect pixel stripes with the same color.
    for path in paths:
        new_path = []
        act_stripe = []
        act_pixel = path['path'][0]
        act_stripe.append(act_pixel)
        for pixel in path['path']:
            if act_pixel['x'] == pixel['x'] and act_pixel['y'] + 1 == pixel['y']:
                act_stripe.append(pixel)
                act_pixel = pixel
            else:
                if act_stripe != [act_pixel]:
                    new_path.append(act_stripe.copy())
                    act_stripe = [pixel]
                    act_pixel = pixel
        new_path.append(act_stripe.copy())
        path['path'] = new_path.copy()
    
    return paths


def simplicity_stripes(paths):
    """convert stripe to be more simple:
    [p1, p2, p3, .... , pn] -> [p1, pn] """
    for path in paths:
        new_path = []
        for stripe in path['path']:
            new_path.append([{'x': stripe[0]['x'], 'y': stripe[0]['y']}, {'x': stripe[-1]['x'], 'y': stripe[-1]['y']}])
        path['path'] = new_path.copy()

    return paths


def detect_blobs(paths):
    # create form stripes blobs.
    for path in paths:
        act_path = path['path']
        new_path = []
        while len(act_path) > 0:
            new_blob = []
            act_stripe = act_path[0]
            
            new_blob.append(act_stripe.copy())
            for stripe in act_path:
                if act_stripe[0]['y'] <= stripe[0]['y'] <= act_stripe[-1]['y']\
                        and act_stripe[0]['x'] + 1 == stripe[0]['x'] \
                        or act_stripe[0]['y'] <= stripe[-1]['y'] <= act_stripe[-1]['y'] \
                        and act_stripe[0]['x'] + 1 == stripe[0]['x']:

                    act_stripe = stripe.copy()
                    new_blob.append(stripe.copy())

            new_path.append(new_blob.copy())
            for stripe in new_blob:
                if stripe in act_path:
                    act_path.remove(stripe)
        
        path['path'] = new_path.copy()
    
    return paths


def convert_paths_to_real(paths, resolution):
    # convert paths structure from pixel to real values.
    for path in paths:
        for blob in path['path']:
            for stripe in blob:
                for pixel in stripe:
                    pixel['x'] = round(pixel['x'] * resolution, 3)
                    pixel['y'] = round(pixel['y'] * resolution, 3)
    
    return paths


def create_blob_contour(paths):
    # create contours from blobs
    new_paths = []

    for path in paths:
        new_path = []
        for blob in path['path']:
            border = []
            for stripe in blob:
                new_stripe = stripe[0].copy()
                border.append(new_stripe)

            for stripe in reversed(blob):
                new_stripe = stripe[1].copy()
                border.append(new_stripe)

            new_path_constr = {'border': border, 'blob': blob}
            new_path.append(new_path_constr.copy())
        new_paths.append({'color': path['color'], 'path': new_path})

    paths = new_paths
    return paths


def create_blob_infill(paths):
    # create infill from blob.
    for path in paths:
        for area in path['path']:
            infill = []
            for n_stripe in range(len(area['blob'])):
                if n_stripe % 2 == 0:
                    infill.append(area['blob'][n_stripe][0].copy())
                    infill.append(area['blob'][n_stripe][1].copy())
                else:
                    infill.append(area['blob'][n_stripe][1].copy())
                    infill.append(area['blob'][n_stripe][0].copy())

            area['infill'] = infill.copy()
    
    return paths


def generate_gcode(paths):
    # generate g-code from paths structure
    g_code = ''
    n_row = 0
    g_code += '%\n'
    for path in paths:
        for area in path['path']:
            n_row += 1
            g_code += f"N{n_row} G01 Z10 F500\n"
            n_row += 1
            g_code += f"N{n_row} G01 X{area['border'][0]['x']} Y{area['border'][0]['y']} Z10 F500\n"
            n_row += 1
            g_code += f"N{n_row} G01 X{area['border'][0]['x']} Y{area['border'][0]['y']} Z0 F500\n"
            for border in area['border']:
                n_row += 1
                g_code += f"N{n_row} G01 X{border['x']} Y{border['y']} Z0 F500\n"
            n_row += 1
            g_code += f"N{n_row} G01 X{area['border'][0]['x']} Y{area['border'][0]['y']} Z0 F500\n"

            for infill in area['infill']:
                n_row += 1
                g_code += f"N{n_row} G01 X{infill['x']} Y{infill['y']} Z0 F500\n"
        n_row += 1
        g_code += f"N{n_row} M01\n"
    g_code += f'N{n_row+1} M30\n'
    g_code += '%\n'

    return g_code


def convert_image_to_path(image_path, resolution):
    # Get image with settings data and return g-code.
    tuple_data = load_image(image_path)
    image_matrix = tuple_data[0]
    image_size = tuple_data[1]
    paths = order_image_by_colors(image_matrix, image_size)
    paths = detect_y_stripes(paths)
    paths = simplicity_stripes(paths)
    paths = detect_blobs(paths)
    paths = convert_paths_to_real(paths, resolution)
    paths = create_blob_contour(paths)
    paths = create_blob_infill(paths)
    g_code = generate_gcode(paths)

    return g_code


print(convert_image_to_path('25_2.png', 0.4))
