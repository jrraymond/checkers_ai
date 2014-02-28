from random import randrange
 
class Board:

  def __init__(self):
    self.board = [[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [0,0,0,0],
                  [0,0,0,0],
                  [2,2,2,2],
                  [2,2,2,2],
                  [2,2,2,2]]


  def __str__(self):
    s = ""
    k = 0
    s = "   0 1 2 3 4 5 6 7\n"
    for i in range(8):
      s += str(i)+" "
      for j in range(8):
        if k % 2 == 1: piece = " "
        elif self.board[i][j/2] == 0: piece = "_"
        else: piece = str(self.board[i][j/2])
        s += "|" + piece
        k+=1
      k+=1
      s += "|\n"
    return s

  """
  Makes a move
    @int player the player making the move
    @int r the start row
    @int c the start column
    @int r1 the end row
    @int c1 the end column
    @(bool,int,int) last tuple with informatin about last move
    @return (bool,bool,int,int) bool 1 indicates succesful move,
      bool 2 indicates if a jump was made, and
      ints indicate location of jumped piece.
  """
  def move(self, player, r, c, r1, c1, last):
    m = self.isLegal(player, r, c, r1, c1)
    jumped = m[1]
    if last[1] and (r != last[2] or c != last[3] or not m[1]):
      return (False,last[1],last[2],last[3])
    if m[0]:
      print "("+str(r)+","+str(c)+") -> ("+str(r1)+","+str(c1)+")"
      if jumped:
        self.board[m[2]][m[3]] = 0
      self.board[r][c] = 0
      self.board[r1][c1] = player
      return (True,jumped,r1,c1)
    else:
      return (False,jumped,r1,c1)

  """
  Determines if a move is legal and provides additional information 
  about the move.
    @int player the player making the move
    @int r the start row
    @int c the start column
    @int r1 the end row
    @int r2 the end column
    @return (bool,bool,int,int) bool 1 indicates valid move,
          bool 2 indicates if someone was jumped,
          int 1 is row of jumped piece, -1 if none,
          int 2 is column of jumped piece, -1 if none.
  """
  def isLegal(self, player, r, c, r1, c1):

    if not self.isInBounds(r,c) or not self.isInBounds(r1,c1):
      return (False,False,-1,-1)

    if (player != self.board[r][c] and player + 2 != self.board[r][c]) or self.board[r1][c1] != 0:
      return (False,False,-1,-1)
    
    if player == 1 or (player > 2 and r1 > r):     #down direction
      if r1 <= r or r1 > r + 2: return (False,False,-1,-1)
      elif r1 == r + 1: 
        if r % 2 == 0 and c1 != c and c1 != c - 1:
          return (False,False,-1,-1)
        elif r % 2 == 1 and c1 != c and c1 != c + 1: 
          return (False,False,-1,-1)
      else: #jump
        if r % 2 == 0: #even row
          if (c1 == c or c1 == c - 1) and self.isInBounds(r+1,c-1) and self.board[r+1][c-1] == 2: return (True,True,r+1,c-1)
          elif (c1 == c or c1 == c + 1) and self.isInBounds(r+1,c) and self.board[r+1][c] == 2: return (True,True,r+1,c)
          else: return (False,False,-1,-1)
        else: #odd row
          if (c1 == c or c1 == c - 1) and self.isInBounds(r+1,c) and self.board[r+1][c] == 2: return (True,True,r+1,c)
          elif (c1 == c or c1 == c + 1) and self.isInBounds(r+1,c+1) and self.board[r+1][c+1] == 2: return (True,True,r+1,c+1)
          else: return (False,False,-1,-1)
        
    if player == 2 or (player > 2 and r1 < r):   #up direction
      if r1 >= r or r1 < r - 2: return (False,False,-1,-1)
      elif r1 == r - 1:
        if r % 2 == 0 and c1 != c and c1 != c - 1:
          return (False,False,-1,-1)
        elif r % 2 == 1 and c1 != c and c1 != c + 1: 
          return (False,False,-1,-1)
      else: #jump
        if r % 2 == 0: #even row
          if (c1 == c or c1 == c -1) and self.isInBounds(r-1,c-1) and self.board[r-1][c-1] == 1: return (True,True,r-1,c-1)
          elif (c1 == c or c1 == c + 1) and self.isInBounds(r-1,c) and self.board[r-1][c] == 1: return (True,True,r-1,c)
          else: return (False,False,-1,-1)
        else: #odd row
          if (c1 == c or c1 == c -1) and self.isInBounds(r-1,c) and self.board[r-1][c] == 1: return (True,True,r-1,c)
          elif (c1 == c or c1 == c + 1) and self.isInBounds(r-1,c-1) and self.board[r-1][c-1] == 1: return (True,True,r-1,c-1)
          else: return (False,False,-1,-1)

    return (True,False,-1,-1);
  
  """
  Turns pieces on baseline of opposite end of board into kings
  """
  def makeKings(self):
    for c in range(4):
      if self.board[0][c] == 2: self.board[0][c] = 4
      if self.board[7][c] == 1: self.board[7][c] = 3
  
  """
  Checks if a row and column are in bounds
  """
  def isInBounds(self,r,c):
    return r >= 0 and r < 8 and c >= 0 and c < 4
  
  """
  Checks if game is over
  """
  def isOver(self):
    p1 = True
    p2 = True
    for r in range(8):
      for c in range(4):
        if self.board[r][c] == 1 or self.board[r][c] == 3: p1 = False
        if self.board[r][c] == 2 or self.board[r][c] == 4: p2 = False
    return p1 or p2


def main():
  b = Board()
  p = 1
  last = (True,False,-1,-1)
  while not b.isOver():
    r = randrange(0,7) #int(raw_input("player "+str(p)+" from row: "))
    c = randrange(0,7) #int(raw_input("player "+str(p)+" from col: "))
    r1 = randrange(0,7) #int(raw_input("player "+str(p)+" to row: "))
    c1 = randrange(0,7) #int(raw_input("player "+str(p)+" to col: "))
    last = b.move(p,r,c/2,r1,c1/2,last)
    if not last[0] or not last[1]: p = 1 if p == 2 else 2
    if not last[0]: last = (False, False, -1, -1)
    b.makeKings()
    if last[0]:
      print b
  print "All Done"


if __name__ == "__main__":
  main()

  #this is a test
