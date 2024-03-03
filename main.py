matrix=[[0 for _ in range(3)] for _ in range(3)]


#numeral matrix
num_mat=dict()

def get_numeral(coords,mat=matrix):
    global num_mat
    
    for i,_ in enumerate(matrix):
        for j,_ in enumerate(_):
            num_mat|={i*3+j+1:[i,j]}
    
    return mat[(num_mat[coords])[0]][(num_mat[coords])[1]]

def change(coords, to):
    
    matrix[(num_mat[coords])[0]][(num_mat[coords])[1]]=to






def val(x):
    d={0:' ',1:'X',4:'O'}
    return d[x]

def print_mat(mat):
    for index,i in enumerate(matrix[::-1]):
        print(' | '.join(map(val,i)))
        print('-'*9 if index!=2 else '')



def check(mat=matrix):
    if all(map(lambda x: True if all(x) else False,mat)):
        print('TIE!')
        return True
    result=''
    winner= lambda x:'X' if x==3 else 'O' if x==12 else ''
    for index,i in enumerate(matrix):
        
        diagonal1=0
        diagonal2=0
        vert=0
        for j_index,_ in enumerate(i):
            diagonal1+=mat[j_index][j_index]
            diagonal2+=mat[j_index][-j_index-1]
            vert+=mat[j_index][index]
        result+=(winner(sum(mat[index])))
        result+=(winner(diagonal1))
        result+=(winner(diagonal2))
        result+=(winner(vert))
            
    if result:
        print(f'{result[0]} WINS!!!')
        return True
    return False
            


def main():
    d={True:'X',False:'O'}
    x_move=True
    while True:
        print_mat(matrix)
        
        if check():
            break

        print(f'{d[x_move]} move')
        try:
            inp=int(input('enter the coords: '))
            if get_numeral(inp)==0:
                change(inp,(1 if x_move else 4))
            else:
                print(f"{d[x_move]} YOU MOVED INTO EXISTING FIELD! Try again")
                x_move=not x_move
        except:
            print('Ты дурак?')
            x_move= not x_move
        x_move=not x_move

    
    
main()