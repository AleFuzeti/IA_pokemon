import csv
import numpy as np

pokemon_types = [
                 "Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

damage_array = np.array([
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                 [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                 [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                 [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                 [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                 [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                 [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                 [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                 [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                 [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                 [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                 [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                 [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                 [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                 [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                 [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]])

def get_pokemon_info(pokemon_id):
    with open('pok_gen1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row[0].lstrip("0") == pokemon_id:
                return row

def calculate_multiplier(attacker_types, defender_types):
    multiplier = 0
    for attacker_type in attacker_types:
        attacker_index = pokemon_types.index(attacker_type)
        damage_multiplier = 1
        for defender_type in defender_types:
            defender_index = pokemon_types.index(defender_type)
            damage_multiplier *= damage_array[attacker_index][defender_index]
        if damage_multiplier > multiplier:
            multiplier = damage_multiplier
    return multiplier

def calc_damage(attacker_info, defender_info, damage_multiplier):
    level = 1
    atkpower = 50
    stab = 1.5
    atkstat = int(attacker_info[5])
    defstat = int(defender_info[6])
    spatkstat = int(attacker_info[7])
    spdefstat = int(defender_info[8])
    damage_atk = (((((2 * level) / 5 + 2) * atkstat * atkpower / defstat) / 50) + 2) * stab * damage_multiplier
    damage_spatk = (((((2 * level) / 5 + 2) * spatkstat * atkpower / spdefstat) / 50) + 2) * stab * damage_multiplier
    if damage_atk > damage_spatk:
        damage = damage_atk
    else:
        damage = damage_spatk
    return damage

def main():
    with open('pok_gen1_w.csv', mode='w', newline='') as wfile:
        writer = csv.writer(wfile, delimiter=';')
        writer.writerow(['ID', 'Nome', 'Tipo(s)', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Win'])

        defender_id = "83"  # ID do Pokémon defensor (Farfetch'd)
        defender_info = get_pokemon_info(defender_id)

        if defender_info is None:
            print("ID do Pokemon defensor não encontrado.")
            return

        defender_types = eval(defender_info[2])
        for attacker_id in range(1, 152):  # Iterar sobre todos os IDs de Pokémon de 1 a 151
            attacker_info = get_pokemon_info(str(attacker_id))
            if attacker_info is None:
                print(f"ID {attacker_id} do Pokemon atacante não encontrado.")
                continue
            
            attacker_types = eval(attacker_info[2])  # Convertendo a string em uma lista Python

            damage_multiplier = calculate_multiplier(attacker_types, defender_types)
            damage = calc_damage(attacker_info, defender_info, damage_multiplier)
            damage_multiplier2 = calculate_multiplier(defender_types, attacker_types)
            damage2 = calc_damage(defender_info, attacker_info, damage_multiplier2)
            
            aux_hp1 = int(attacker_info[4])
            aux_hp2 = int(defender_info[4])
            while True:
                aux_hp1 -= damage2
                aux_hp2 -= damage
                if aux_hp1 <= 0:
                    writer.writerow(attacker_info + ['0'])  # O Pokémon atacante perdeu
                    break
                if aux_hp2 <= 0:
                    writer.writerow(attacker_info + ['1'])  # O Pokémon atacante venceu
                    break
                damage = calc_damage(attacker_info, defender_info, damage_multiplier)
                damage2 = calc_damage(defender_info, attacker_info, damage_multiplier2)

if __name__ == "__main__":
    main()