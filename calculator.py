
print("ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ [lexa] ï¿½ [lexa]") 

def subtraction(a, b):
    result = a - b
    return f"{a} - {b} = {result}"

print(subtraction(8, 2))
print("Êàëüêóëÿòîð êîìàíäû [òâîå èìÿ] è [èìÿ äðóãà]")

def add(a, b):
    """Ôóíêöèÿ ñëîæåíèÿ äâóõ ÷èñåë"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

# Ïðîâåðêà ðàáîòû
if __name__ == "__main__":
    print("Ïðîâåðÿåì ñëîæåíèå:")
    add(5, 3)
    add(10, 20)
