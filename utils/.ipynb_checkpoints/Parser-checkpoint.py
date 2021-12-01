
class Parser():
    def __init__(self):
        pass

    def create_round_winner_columns(self, dataset):
        dataset["roundwinner_bin"] = dataset["round_winner"].apply(
            lambda el:
                1 if el == "CT"
                else 0
        )
        dataset["round_winner_ct"] = dataset["round_winner"].apply(
            lambda el:
                1 if el == "CT"
                else 0
        )
        dataset["round_winner_t"] = dataset["round_winner"].apply(
            lambda el:
                1 if el == "T"
                else 0
        )
        return dataset

    def classify_weapons(self, dataset):
        dataset["t_main_rifle"] = (
            dataset["t_weapon_ak47"]
            + dataset["t_weapon_aug"]
            + dataset["t_weapon_m4a4"]
            + dataset["t_weapon_m4a1s"]
            + dataset["t_weapon_sg553"]
        )
        # Concatenating all ct sec rifles
        dataset["t_sec_rifle"] = (
            dataset["t_weapon_galilar"] + dataset["t_weapon_famas"]
        )
        # Concatenating all t normal force buy weapons
        dataset["t_force_weapons"] = (
            dataset["t_weapon_ssg08"]
            + dataset["t_weapon_mp9"]
            + dataset["t_weapon_mac10"]
            + dataset["t_weapon_mp7"]
            + dataset["t_weapon_ump45"]
            + dataset["t_weapon_p90"]
            + dataset["t_weapon_mp5sd"]
            + dataset["t_weapon_mag7"]
            + dataset["t_weapon_nova"]
            + dataset["t_weapon_xm1014"]
        )
        # Concatenating all t extra weak pistols
        dataset["t_weak_pistols"] = (
            dataset["t_weapon_p250"]
            + dataset["t_weapon_tec9"]
            + dataset["t_weapon_fiveseven"]
            + dataset["t_weapon_cz75auto"]
        )
        # Concatenating all t extra strong pistols
        dataset["t_strong_pistols"] = (
            dataset["t_weapon_deagle"] + dataset["t_weapon_r8revolver"]
        )
        dataset["t_granades"] = (
            dataset["t_grenade_hegrenade"]
            + dataset["t_grenade_flashbang"]
            + dataset["t_grenade_smokegrenade"]
            + dataset["t_grenade_incendiarygrenade"]
            + dataset["t_grenade_molotovgrenade"]
        )
        # Concatenating all ct main rifles
        dataset["ct_main_rifle"] = (
            dataset["ct_weapon_ak47"]
            + dataset["ct_weapon_aug"]
            + dataset["ct_weapon_m4a4"]
            + dataset["ct_weapon_m4a1s"]
            + dataset["ct_weapon_sg553"]
        )
        # Concatenating all ct sec rifles
        dataset["ct_sec_rifle"] = (
            dataset["ct_weapon_galilar"] + dataset["ct_weapon_famas"]
        )

        # Concatenating all ct normal force buy weapons
        dataset["ct_force_weapons"] = (
            dataset["ct_weapon_ssg08"]
            + dataset["ct_weapon_mp9"]
            + dataset["ct_weapon_mac10"]
            + dataset["ct_weapon_mp7"]
            + dataset["ct_weapon_ump45"]
            + dataset["ct_weapon_p90"]
            + dataset["ct_weapon_mp5sd"]
            + dataset["ct_weapon_mag7"]
            + dataset["ct_weapon_nova"]
            + dataset["ct_weapon_xm1014"]
        )
        # Concatenating all t extra weak pistols
        dataset["ct_weak_pistols"] = (
            dataset["ct_weapon_p250"]
            + dataset["ct_weapon_tec9"]
            + dataset["ct_weapon_fiveseven"]
            + dataset["ct_weapon_cz75auto"]
        )
        # Concatenating all t extra strong pistols
        dataset["ct_strong_pistols"] = (
            dataset["ct_weapon_deagle"] + dataset["ct_weapon_r8revolver"]
        )
        # Concatenating all grenades
        dataset["ct_granades"] = (
            dataset["ct_grenade_hegrenade"]
            + dataset["ct_grenade_flashbang"]
            + dataset["ct_grenade_smokegrenade"]
            + dataset["ct_grenade_incendiarygrenade"]
            + dataset["ct_grenade_molotovgrenade"]
        )
        return dataset