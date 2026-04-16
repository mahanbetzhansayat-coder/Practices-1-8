# Parent 1
class Father:
    def skill_1(self):
        print("I am good at sports (from Father).")

# Parent 2
class Mother:
    def skill_2(self):
        print("I am good at art (from Mother).")

# Child inherits from BOTH
class Child(Father, Mother):
    def skill_3(self):
        print("I am good at coding (Child's own skill).")

# --- Testing ---
kid = Child()

print("--- Kid's Skills ---")
kid.skill_1()
kid.skill_2()
kid.skill_3()