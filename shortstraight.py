myhand = [2,2,3,3,5]
selection = 'short straight'
shortstraight = 0 
#possible short straights
straightone = [1,2,3,4,'x']
straighttwo = ['x',2,3,4,5]
straightthree = ['x',3,4,5,6]
straightfour = ['x',1,2,3,4]
straightfive = [2,3,4,5,'x']
straightsix = [3,4,5,6,'x']
#checks against all possible short straights 
if selection == 'short straight':
    if myhand[0:4] == straightone[0:4]:
       print('short straight!')
       shortstraight = 30
       
    elif myhand[0:4] == straightfive[0:4]:
       print('short straight!')
       shortstraight = 30

    elif myhand[0:4] == straightsix[0:4]:
       print('short straight!')
       shortstraight = 30

    elif myhand[1:5] == straighttwo[1:5]:
       print('short straight!')
       shortstraight = 30

    elif myhand[1:5] == straightthree[1:5]:
       print('short straight!')
       shortstraight = 30

    elif myhand[1:5] == straightfour[1:5]:
       print('short straight!')
       shortstraight = 30

    else:
        print('not a short straight you little water buffolooouuu')
        
print('you get',shortstraight,' points!!')
