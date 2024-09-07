import fila_alunos
import stack_alunos

def is_palindrome(s):
    stk = stack_alunos.StackUsingListEnd()
    q = fila_alunos.QueueUsingDeque()
    for ch in "".join(s.lower().split()):
        stk.push(ch)
        q.enqueue(ch)
    while not stk.is_empty():
        if stk.pop() != q.dequeue():
            return False
    return True

def main():
    strings = ["ABBA",
               "whatever",
               "Amor a Roma",
               "Anotaram a data da maratona",
               "O lobo ama o bolo",
               "Arara"]       

    for s in strings:
        print(f"'{s}' é um palíndroma? {is_palindrome(s)}")                

if __name__ == "__main__":
    main()