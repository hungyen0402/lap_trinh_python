import re
def solve():
    dict = {}
    input_text = input().strip()
    # print(input_text)
    sentences = re.split(r'[-,.?!:;/]', input_text) # chú ý dấu - 
    print(sentences)      
    for sentence in sentences:
        sentence = sentence.strip()
        print(sentence)

    

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()