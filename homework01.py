
# 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

first_side = int(input("Длина первой стороны: "))
second_side = int(input("Длина второй стороны: "))
third_side = int(input("Длина третьей стороны: "))

if first_side >= second_side + third_side or second_side >= first_side + third_side or third_side >= first_side + second_side:
    print("Такого треугольника не существует.")
elif first_side == second_side and first_side == third_side:
    print("Треугольник равносторонний.")
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print("Треугольник равнобедренный.")
else:
    print("Треугольник разносторонний.")
