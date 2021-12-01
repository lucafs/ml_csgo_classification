def define_full_ct_eco(row):
    """Nothing other than pistols and less than 3 people with armor and strong pistol"""
    if (
        (row["ct_force_weapons"] + row["ct_main_rifle"] + row["ct_weapon_awp"] == 0)
        and (row["ct_armor"] < 3)
        and (row["ct_strong_pistols"] < 3)
        and (row["pistol_round"] == 0)
    ):
        return 1
    else:
        return 0

def define_full_t_eco(row):
    """Nothing other than pistols and less than 3 people with armor and strong pistol"""
    if (
        (
            row["t_force_weapons"]
            + row["t_main_rifle"]
            + row["t_weapon_awp"]
            + row["t_strong_pistols"]
            == 0
        )
        and (row["t_armor"] < 3)
        and (row["pistol_round"] == 0)
    ):
        return 1
    else:
        return 0

def define_force_ct_round(row):
    """Less than 3 medium rifle, no strong rifles or awp and not more than 13 granades"""
    if (
        (row["ct_force_weapons"] + row["ct_sec_rifle"] > 3)
        and (row["ct_sec_rifle"] < 3)
        and (row["ct_main_rifle"] == 0)
        and (row["ct_weapon_awp"] == 0)
        and (row["ct_granades"] < 13)
    ):
        return 1
    else:
        return 0

def define_force_t_round(row):
    """Less than 3 medium rifle, no strong rifles or awp and not more than 13 granades"""
    if (
        (row["t_force_weapons"] + row["t_sec_rifle"] > 3)
        and (row["t_sec_rifle"] < 3)
        and (row["t_main_rifle"] == 0)
        and (row["t_weapon_awp"] == 0)
        and (row["t_granades"] < 13)
    ):
        return 1
    else:
        return 0

def define_pistol_round(row):
    if (
        (row["ct_score"] + row["t_score"]) == 0
        or (row["ct_score"] + row["t_score"]) == 15
    ):
        return 1
    else:
        return 0