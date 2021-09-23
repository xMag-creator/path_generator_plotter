from random import randint
from machine_app.models import Machine


def fake_machine_data():
    return {
        "name": f"machine{randint(1, 100)}",
        "x_max_range": randint(1, 10000) / 100,
        "x_min_range": 0,
        "y_max_range": randint(1, 10000) / 100,
        "y_min_range": 0,
        "z_max_range": randint(1, 10000) / 100,
        "z_min_range": 0,
        "u_max_range": randint(1, 360),
        "u_min_range": randint(1, 360),
        "v_max_range": randint(1, 360),
        "v_min_range": randint(1, 360),
        "w_max_range": randint(1, 360),
        "w_min_range": randint(1, 360),
        "z_push_pos": randint(1, 2000) / 100,
        "z_jump_lim": randint(1, 10000) / 100,
        "x_sheet_offset": randint(1, 10000) / 100,
        "y_sheet_offset": randint(1, 10000) / 100,

    }


def create_fake_machine():
    machine_data = fake_machine_data()
    Machine.objects.create(**machine_data)


def fake_range():
    return randint(1, 10000) / 100
