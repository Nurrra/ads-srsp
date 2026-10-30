def hanoi(n, source, target, helper):
    if n == 0:
        return
    hanoi(n - 1, source, helper, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, helper, target, source)

hanoi(3, "A", "B", "C")