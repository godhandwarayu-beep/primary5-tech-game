import json
import random

def load_game_data():
    with open("game_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def character_selection():
    print("========================================")
    print("  ยินดีต้อนรับสู่เกม 3D RPG: ดิจิทัลฮีโร่ ป.5  ")
    print("========================================")
    name = input("กรุณากรอกชื่อตัวละครของคุณ: ")
    print("\nเลือกเพศตัวละคร:")
    print("1. ตัวละครชาย (Hero)")
    print("2. ตัวละครหญิง (Heroine)")
    choice = input("เลือกหมายเลข (1 หรือ 2): ")
    
    char_gender = "ชาย" if choice == "1" else "หญิง"
    print(f"\nยินดีต้อนรับคุณ {name} ({char_gender}) สู่การผจญภัยพิทักษ์อาณาจักรเทคโนโลยี!")
    return name, char_gender

def battle_with_boss(level_info):
    print(\n"----------------------------------------")
    print(f"🚩 {level_info['title']}")
    print(f"🎯 ภารกิจ: {level_info['mission']} - {level_info['description']}")
    print(f"👾 บอสประจำด่านปรากฏตัว: {level_info['boss']}!")
    print("----------------------------------------")
    
    boss_hp = 50 + (level_info['level'] * 5)
    player_hp = 100
    
    while boss_hp > 0 and player_hp > 0:
        print(f"\n[สถานะ] พลังชีวิตของคุณ: {player_hp} | พลังชีวิตบอส ({level_info['boss']}): {boss_hp}")
        print("เลือกคำสั่งต่อสู้:")
        print("1. โจมตีด้วยคีย์บอร์ดเวทมนตร์ (Normal Attack)")
        print("2. ใช้สกิลตอบคำถามความรู้ ป.5 (Skill Attack)")
        print("3. ป้องกัน (Defend)")
        
        action = input("เลือกหมายเลข (1-3): ")
        
        if action == "1":
            damage = random.randint(15, 25)
            boss_hp -= damage
            print(f"💥 คุณโจมตีใส่ {level_info['boss']} สร้างความเสียหาย {damage} แต้ม!")
        elif action == "2":
            damage = random.randint(25, 40)
            boss_hp -= damage
            print(f"✨ คุณใช้สกิลตอบคำถามถูกต้อง! สร้างความเสียหายรุนแรง {damage} แต้ม!")
        elif action == "3":
            print("🛡️ คุณตั้งท่าป้องกัน ลดความเสียหายที่จะได้รับในเทิร์นนี้ลงครึ่งหนึ่ง!")
        else:
            print("⚠️ เลือกคำสั่งไม่ถูกต้อง เสียเทิร์นฟรี!")
            
        if boss_hp > 0:
            boss_damage = random.randint(10, 20)
            if action == "3":
                boss_damage //= 2
            player_hp -= boss_damage
            print(f"⚡ {level_info['boss']} โต้กลับ! สร้างความเสียหายให้คุณ {boss_damage} แต้ม")
            
    if player_hp > 0:
        print(f"\n🎉 ยินดีด้วย! คุณพิชิต {level_info['boss']} สำเร็จในด่านนี้แล้ว!")
        return True
    else:
        print(f"\n💀 คุณพ่ายแพ้ให้กับ {level_info['boss']}... ลองใหม่อีกครั้งนะ!")
        return False

def main():
    data = load_game_data()
    name, gender = character_selection()
    
    all_levels = data["term_1"]["levels"] + data["term_2"]["levels"]
    
    for lvl in all_levels:
        success = battle_with_boss(lvl)
        if not success:
            print("\nเกมโอเวอร์! กลับไปทบทวนบทเรียนแล้วมาลุยใหม่นะฮีโร่")
            break
        cont = input("\nต้องการผจญภัยในด่านถัดไปหรือไม่? (y/n): ")
        if cont.lower() != 'y':
            print("บันทึกการเดินทางเรียบร้อยแล้ว ไว้กลับมาลุยต่อใหม่นะ!")
            break
    else:
        print(f"\n🏆 สุดยอดมาก! คุณ {name} พิชิตครบทั้ง 40 ด่าน กลายเป็นสุดยอดดิจิทัลฮีโร่ประจำโรงเรียนแล้ว!")

if __name__ == "__main__":
    main()