"""
4_2______
____6____
_589_____
_9__5__8_
___34__51
_________
__16__32_
_8_1_____
3_62__9_4



"""

#Neccicary libraries for all solutions
import sys
import math
import string

### DELETE AFTER TESING
sys.path.append('D:\\CodeQuest')
import inputs
inputs.init("inputs")
####
"""
chunks = 

[
1  4  7
2  5  8
3  6  9
]





"""


class number():
    def __init__(self:iter, value:int, row_id:int, column_id:int, chunk_id:int,) -> None:
        if value == "_":
            self.filled = False
        else:
            self.filled = True
            
        self.row_id = row_id
        self.column_id = column_id
        self.chunk_id = chunk_id




class sudoku:
    def __init__(self):
        self.rows = []
        self.columns = [[],[],[],[],[],[],[],[],[],] 
        self.chunks = []   
        self.numbers = []
    def add_row(self:iter, row:str):
        self.rows.append([i for i in row])
        for i,obj in enumerate(row): 
            self.columns[i].append(obj)   #ads the new number to each column
        
    def finalize(self):
        chunk_id = 0
        for column in range(0,3):
            for row in range(0,3):
                chunk = []
                 
                for x in range(0,3):
                    for y in range(0,3):

                        chunk.append(self.rows[x+row*3][y+column*3])
                        
                        self.numbers.append(number(value=self.rows[x+row*3][y+column*3], row_id=[x+row*3],column_id=[y+column*3],chunk_id=chunk_id))
                self.chunks.append(chunk)
                chunk_id += 1

    def check_for_spaces(self):
        for i in self.numbers:
            if i.filled == False:
                return False
        return True
    def fill(self:iter):
        while self.check_for_spaces() == False:
            
            for i in self.numbers:
                if i.filled != False:
                    print("not filled")
            break    


#input
#cases = int(sys.stdin.readline().rstrip())    ##IMPORANT: UNCOMMENT AFTER TESTING
cases = int(inputs.input())   #Test Line

for case in range(cases):
    
    #sys.stdin.readline().rstrip()) ##IMPORANT: UNCOMMENT AFTER TESTING
    board = sudoku()
    for i in range(0,9):
        board.add_row(inputs.input()) # Test Line
    board.finalize()
    board.fill()
    
    
    
