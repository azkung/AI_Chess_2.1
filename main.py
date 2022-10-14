'''
Programmed by Alexander Kung
'''

import sys
import pygame
import random
import copy
import math

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 800,800
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('AI Chess')

WHITE = (255,255,255)
DARKGREEN = (119, 149, 86)
LIGHTGREEN = (235, 236, 208)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

turn = -1

pieces = pygame.image.load('chessPieces.jpg')

'''
whitePawn = pygame.image.load('whitePawn.png')
whiteRook = pygame.image.load('whiteRook.png')
whiteKnight = pygame.image.load('whiteKnight.png')
whiteBishop = pygame.image.load('whiteBishop.png')
whiteQueen = pygame.image.load('whiteQueen.png')
whiteKing = pygame.image.load('whiteKing.png')

blackBishop = pygame.image.load('blackBishop.png')
blackKing = pygame.image.load('blackKing.png')
blackKnight = pygame.image.load('blackKnight.png')
blackPawn = pygame.image.load('blackPawn.png')
blackQueen = pygame.image.load('blackQueen.png')
blackRook = pygame.image.load('blackRook.png')
'''


whitePawn = pygame.image.load('white-pawn.png')
whiteRook = pygame.image.load('white-rook.png')
whiteKnight = pygame.image.load('white-knight.png')
whiteBishop = pygame.image.load('white-bishop.png')
whiteQueen = pygame.image.load('white-queen.png')
whiteKing = pygame.image.load('white-king.png')

blackBishop = pygame.image.load('black-bishop.png')
blackKing = pygame.image.load('black-king.png')
blackKnight = pygame.image.load('black-knight.png')
blackPawn = pygame.image.load('black-pawn.png')
blackQueen = pygame.image.load('black-queen.png')
blackRook = pygame.image.load('black-rook.png')


whitePawn = pygame.transform.scale(whitePawn, (100, 100))
whiteRook = pygame.transform.scale(whiteRook, (100, 100))
whiteKnight = pygame.transform.scale(whiteKnight, (100, 100))
whiteBishop = pygame.transform.scale(whiteBishop, (100, 100))
whiteQueen = pygame.transform.scale(whiteQueen, (100, 100))
whiteKing = pygame.transform.scale(whiteKing, (100, 100))

blackPawn = pygame.transform.scale(blackPawn, (100, 100))
blackRook = pygame.transform.scale(blackRook, (100, 100))
blackKnight = pygame.transform.scale(blackKnight, (100, 100))
blackBishop = pygame.transform.scale(blackBishop, (100, 100))
blackQueen = pygame.transform.scale(blackQueen, (100, 100))
blackKing = pygame.transform.scale(blackKing, (100, 100))


def scoreCalcBasic(board):
    currentScore = 0

    for i in board:
        for j in i:
            if j > 0:
                if abs(j) == 1:
                    currentScore += 1
                if abs(j) == 2:
                    currentScore += 3
                if abs(j) == 3:
                    currentScore += 3
                if abs(j) == 4:
                    currentScore += 5
                if abs(j) == 5:
                    currentScore += 9
            if j < 0:
                if abs(j) == 1:
                    currentScore -= 1
                if abs(j) == 2:
                    currentScore -= 3
                if abs(j) == 3:
                    currentScore -= 3
                if abs(j) == 4:
                    currentScore -= 5
                if abs(j) == 5:
                    currentScore -= 9
    return currentScore

def scoreCalcMiddleRush(board):
    currentScore = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                distanceFromCenter = math.sqrt(((i-4.5)**2) + ((j-4.5)**2))
                if abs(board[i][j]) == 1:
                    currentScore += 4
                    currentScore += ((6-round(distanceFromCenter))/30)
                if abs(board[i][j]) == 2:
                    currentScore += 12
                    currentScore += ((6-round(distanceFromCenter))/30)
                if abs(board[i][j]) == 3:
                    currentScore += 12
                    currentScore += ((6-round(distanceFromCenter))/30)
                if abs(board[i][j]) == 4:
                    currentScore += 20
                    currentScore += ((6-round(distanceFromCenter))/30)
                if abs(board[i][j]) == 5:
                    currentScore += 32
                    currentScore += ((6-round(distanceFromCenter))/30)
            if board[i][j] < 0:
                distanceFromCenter = math.sqrt(((i-4.5)**2) + ((j-4.5)**2))
                if abs(board[i][j]) == 1:
                    currentScore -= 4
                    currentScore -= ((6-round(distanceFromCenter))/30)
                if abs(board[i][j]) == 2:
                    currentScore -= 12
                    currentScore -= ((6-round(distanceFromCenter))/30)
                if abs(board[i][j]) == 3:
                    currentScore -= 12
                    currentScore -= ((6-round(distanceFromCenter))/30)
                if abs(board[i][j]) == 4:
                    currentScore -= 20
                    currentScore -= ((6-round(distanceFromCenter))/30)
                if abs(board[i][j]) == 5:
                    currentScore -= 32
                    currentScore -= ((6-round(distanceFromCenter))/30)
    return currentScore

def scoreCalcKingRush(board):
    currentScore = 0

    whiteKingPos = []
    blackKingPos = []


    for i in range(len(board)):
        breakAll = False
        for j in range(len(board[i])):
            if board[i][j] == 6:
                whiteKingPos = [i,j]
            if board[i][j] == -6:
                blackKingPos = [i,j]

            if whiteKingPos != [] and blackKingPos != []:
                breakAll = True
                break
        if breakAll:
            break

    divisor = 25
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                distanceFromKing = math.sqrt(((i-blackKingPos[0])**2) + ((j-blackKingPos[1])**2))
                if abs(board[i][j]) == 1:
                    currentScore += 4
                    currentScore += ((10-round(distanceFromKing))/divisor)
                if abs(board[i][j]) == 2:
                    currentScore += 12
                    currentScore += ((10-round(distanceFromKing))/divisor)
                if abs(board[i][j]) == 3:
                    currentScore += 12
                    currentScore += ((10-round(distanceFromKing))/divisor)
                if abs(board[i][j]) == 4:
                    currentScore += 20
                    currentScore += ((10-round(distanceFromKing))/divisor)
                if abs(board[i][j]) == 5:
                    currentScore += 32
                    currentScore += ((10-round(distanceFromKing))/divisor)
            if board[i][j] < 0:
                distanceFromKing = math.sqrt(((i-whiteKingPos[0])**2) + ((j-whiteKingPos[1])**2))
                if abs(board[i][j]) == 1:
                    currentScore -= 4
                    currentScore -= ((10-round(distanceFromKing))/divisor)
                if abs(board[i][j]) == 2:
                    currentScore -= 12
                    currentScore -= ((10-round(distanceFromKing))/divisor)
                if abs(board[i][j]) == 3:
                    currentScore -= 12
                    currentScore -= ((10-round(distanceFromKing))/divisor)
                if abs(board[i][j]) == 4:
                    currentScore -= 20
                    currentScore -= ((10-round(distanceFromKing))/divisor)
                if abs(board[i][j]) == 5:
                    currentScore -= 32
                    currentScore -= ((10-round(distanceFromKing))/divisor)
    return currentScore

def scoreCalc(board):
    return scoreCalcMiddleRush(board)


def minimax(board, turn, castleData, depth, alpha, beta):
    #White maximizing, Black minimizing

    '''
    isWhiteKing = False
    for i in board:
        if 6 in i:
            isWhiteKing = True
            break
    if not isWhiteKing:
        return [float('-inf'), board, castleData]
    
    isBlackKing = False
    for i in board:
        if -6 in i:
            isBlackKing = True
            break
    if not isBlackKing:
        return [float('inf'), board, castleData]
    ''' 
    
    checkmateCheckData = checkmateCheck(board, castleData)
    if checkmateCheckData == 1:
        #Black Wins
        return [float('-inf'), board, castleData]
    if checkmateCheckData == -1:
        #White Wins
        return [float('inf'), board, castleData]

    inCheck = checkCheck(board, castleData)

    if depth == 0:
        return [scoreCalc(board), board, castleData]

    if turn == 1:
        #Maximizing White
        maxScore = float('-inf')
        maxBoard = copy.deepcopy(board)
        maxCastleData = copy.deepcopy(castleData)

        breakAll = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] > 0:
                    #Is White Piece
                    tempMoves = findMoves(board, board[i][j], i, j, castleData)
                    if board[i][j] == 6:
                        tempMoves = copy.deepcopy(pieceLimit(board, board[i][j], i, j, tempMoves, castleData))
                    tempMoves = copy.deepcopy(checkLimit(board, board[i][j], i, j, tempMoves, castleData))

                    for a in tempMoves:
                        #Duplicate board and do possible move 'a'
                        tempBoard = copy.deepcopy(board)

                        tempBoard[i][j] = 0
                        tempBoard[a[0]][a[1]] = board[i][j]

                        tempCastleData = copy.deepcopy(castleData)

                        if board[i][j] == 6 and tempCastleData[0] == False:
                            tempCastleData[0] = True
                            data = copy.deepcopy(checkCastle(tempBoard, 1, tempCastleData))
                            tempBoard = copy.deepcopy(data[0])
                            tempCastleData = copy.deepcopy(data[1])

                        if board[i][j] == 6:
                            #White King Moved
                            tempCastleData[0] = True
                        if board[i][j] == 4 and i == 0 and j == 7:
                            #White Left Rook Moved
                            tempCastleData[1] = True
                        if board[i][j] == 4 and i == 7 and j == 7:
                            #White Right Rook Moved
                            tempCastleData[2] = True

                        score = minimax(tempBoard, turn*-1, tempCastleData, depth-1, alpha, beta)[0]

                        previousMaxScore = maxScore
                        maxScore = max(score, maxScore)

                        if maxScore != previousMaxScore:
                            maxBoard = copy.deepcopy(tempBoard)
                            maxCastleData = copy.deepcopy(tempCastleData)

                        
                        alpha = max(alpha, score)

                        if beta <= alpha:
                            breakAll = True
                            break
                if breakAll:
                    break
            if breakAll:
                break
        return [maxScore, maxBoard, maxCastleData]                

    if turn == -1:
        #Minimizing Black
        minScore = float('inf')
        minBoard = copy.deepcopy(board)
        minCastleData = copy.deepcopy(castleData)

        breakAll = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] < 0:
                    #Is Black Piece
                    
                    tempMoves = findMoves(board, board[i][j], i, j, castleData)

                    if board[i][j] == -6:
                        tempMoves = copy.deepcopy(pieceLimit(board, board[i][j], i, j, tempMoves, castleData))

                    tempMoves = copy.deepcopy(checkLimit(board, board[i][j], i, j, tempMoves, castleData))

                    for a in tempMoves:
                        #Duplicate board and do possible move 'a'
                        tempBoard = copy.deepcopy(board)

                        tempBoard[i][j] = 0
                        tempBoard[a[0]][a[1]] = board[i][j]

                        tempCastleData = copy.deepcopy(castleData)

                        if board[i][j] == -6 and castleData[3] == False:
                            tempCastleData[3] = True
                            data = copy.deepcopy(checkCastle(tempBoard, -1, tempCastleData))
                            tempBoard = copy.deepcopy(data[0])
                            tempCastleData = copy.deepcopy(data[1])
                        
                        if board[i][j] == -6:
                            #Black King Moved
                            tempCastleData[3] = True
                        if board[i][j] == -4 and i == 0 and j == 0:
                            #Black Left Rook Moved
                            tempCastleData[4] = True
                        if board[i][j] == -4 and i == 7 and j == 0:
                            #Black Right Rook Moved
                            tempCastleData[5] = True

                        score = minimax(tempBoard, turn*-1, tempCastleData, depth-1, alpha, beta)[0]

                        previousMinScore = minScore
                        minScore = min(score, minScore)

                        if minScore != previousMinScore:
                            minBoard = copy.deepcopy(tempBoard)
                            minCastleData = copy.deepcopy(tempCastleData)

                        beta = min(beta, score)
                        if beta <= alpha:
                            breakAll = True
                            break
                if breakAll:
                    break
            if breakAll:
                break
        return [minScore, minBoard, minCastleData]

        

def aiMoveMax(board, turn, castleData):
    #Best move for White

    maxScore = float('-inf')
    

def findMoves(board, name, x, y, castleData):
    possibleMoves = [] #x, y, Kill
    color = 0
    if name > 0:
        color = 1
    if name < 0:
        color = -1

    if name == 1:
        #White Pawn
        if y == 6:
            if x in range(0,8) and y-2 in range(0,8):
                if board[x][y-2] == 0 and board[x][y-1] == 0:
                    possibleMoves.append([x,y-2,False])
            if x in range(0,8) and y-1 in range(0,8):
                if board[x][y-1] == 0:
                    possibleMoves.append([x,y-1,False])
            if x-1 in range(0,8) and y-1 in range(0,8):
                if board[x-1][y-1] < 0:
                    possibleMoves.append([x-1,y-1,True])
            if x+1 in range(0,8) and y-1 in range(0,8):
                if board[x+1][y-1] < 0:
                    possibleMoves.append([x+1,y-1,True])
        else:
            if x in range(0,8) and y-1 in range(0,8):
                if board[x][y-1] == 0:
                    possibleMoves.append([x,y-1,False])
            if x-1 in range(0,8) and y-1 in range(0,8):
                if board[x-1][y-1] < 0:
                    possibleMoves.append([x-1,y-1,True])
            if x+1 in range(0,8) and y-1 in range(0,8):
                if board[x+1][y-1] < 0:
                    possibleMoves.append([x+1,y-1,True])

    elif name == -1:
        if y == 1:
            if x in range(0,8) and y+2 in range(0,8):
                if board[x][y+2] == 0 and board[x][y+1] == 0:
                    possibleMoves.append([x,y+2,False])
            if x in range(0,8) and y+1 in range(0,8):
                if board[x][y+1] == 0:
                    possibleMoves.append([x,y+1,False])
            if x-1 in range(0,8) and y+1 in range(0,8):
                if board[x-1][y+1] > 0:
                    possibleMoves.append([x-1,y+1,True])
            if x+1 in range(0,8) and y+1 in range(0,8):
                if board[x+1][y+1] > 0:
                    possibleMoves.append([x+1,y+1,True])
        else:
            if x in range(0,8) and y+1 in range(0,8):
                if board[x][y+1] == 0:
                    possibleMoves.append([x,y+1,False])
            if x-1 in range(0,8) and y+1 in range(0,8):
                if board[x-1][y+1] > 0:
                    possibleMoves.append([x-1,y+1,True])
            if x+1 in range(0,8) and y+1 in range(0,8):
                if board[x+1][y+1] > 0:
                    possibleMoves.append([x+1,y+1,True])

    elif abs(name) == 2:
        #Knight
        if x+2 in range(0,8) and y+1 in range(0,8):
            if board[x+2][y+1] == 0:
                possibleMoves.append([x+2,y+1,False])
            elif (board[x+2][y+1] > 0 and color < 0) or (board[x+2][y+1] < 0 and color > 0):
                possibleMoves.append([x+2,y+1,True])
        if x+2 in range(0,8) and y-1 in range(0,8):
            if board[x+2][y-1] == 0:
                possibleMoves.append([x+2,y-1,False])
            elif (board[x+2][y-1] > 0 and color < 0) or (board[x+2][y-1] < 0 and color > 0):
                possibleMoves.append([x+2,y-1,True])
        if x-2 in range(0,8) and y+1 in range(0,8):
            if board[x-2][y+1] == 0:
                possibleMoves.append([x-2,y+1,False])
            elif (board[x-2][y+1] > 0 and color < 0) or (board[x-2][y+1] < 0 and color > 0):
                possibleMoves.append([x-2,y+1,True])
        if x-2 in range(0,8) and y-1 in range(0,8):
            if board[x-2][y-1] == 0:
                possibleMoves.append([x-2,y-1,False])
            elif (board[x-2][y-1] > 0 and color < 0) or (board[x-2][y-1] < 0 and color > 0):
                possibleMoves.append([x-2,y-1,True])
        if x+1 in range(0,8) and y-2 in range(0,8):
            if board[x+1][y-2] == 0:
                possibleMoves.append([x+1,y-2,False])
            elif (board[x+1][y-2] > 0 and color < 0) or (board[x+1][y-2] < 0 and color > 0):
                possibleMoves.append([x+1,y-2,True])
        if x+1 in range(0,8) and y+2 in range(0,8):
            if board[x+1][y+2] == 0:
                possibleMoves.append([x+1,y+2,False])
            elif (board[x+1][y+2] > 0 and color < 0) or (board[x+1][y+2] < 0 and color > 0):
                possibleMoves.append([x+1,y+2,True])
        if x-1 in range(0,8) and y+2 in range(0,8):
            if board[x-1][y+2] == 0:
                possibleMoves.append([x-1,y+2,False])
            elif (board[x-1][y+2] > 0 and color < 0) or (board[x-1][y+2] < 0 and color > 0):
                possibleMoves.append([x-1,y+2,True])
        if x-1 in range(0,8) and y-2 in range(0,8):
            if board[x-1][y-2] == 0:
                possibleMoves.append([x-1,y-2,False])
            elif (board[x-1][y-2] > 0 and color < 0) or (board[x-1][y-2] < 0 and color > 0):
                possibleMoves.append([x-1,y-2,True])
    
    elif abs(name) == 5:
        #Queen
        for i in range(1,8):
            if x+i in range(0,8):
                if board[x+i][y] == 0:
                    possibleMoves.append([x+i,y,False])
                elif (board[x+i][y] > 0 and color < 0) or (board[x+i][y] < 0 and color > 0):
                    possibleMoves.append([x+i,y,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x-i in range(0,8):
                if board[x-i][y] == 0:
                    possibleMoves.append([x-i,y,False])
                elif (board[x-i][y] > 0 and color < 0) or (board[x-i][y] < 0 and color > 0):
                    possibleMoves.append([x-i,y,True])
                    break
                else:
                    break

        for i in range(1,8):
            if y+i in range(0,8):
                if board[x][y+i] == 0:
                    possibleMoves.append([x,y+i,False])
                elif (board[x][y+i] > 0 and color < 0) or (board[x][y+i] < 0 and color > 0):
                    possibleMoves.append([x,y+i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if y-i in range(0,8):
                if board[x][y-i] == 0:
                    possibleMoves.append([x,y-i,False])
                elif (board[x][y-i] > 0 and color < 0) or (board[x][y-i] < 0 and color > 0):
                    possibleMoves.append([x,y-i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x-i in range(0,8) and y-i in range(0,8):
                if board[x-i][y-i] == 0:
                    possibleMoves.append([x-i,y-i,False])
                elif (board[x-i][y-i] > 0 and color < 0) or (board[x-i][y-i] < 0 and color > 0):
                    possibleMoves.append([x-i,y-i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x+i in range(0,8) and y+i in range(0,8):
                if board[x+i][y+i] == 0:
                    possibleMoves.append([x+i,y+i,False])
                elif (board[x+i][y+i] > 0 and color < 0) or (board[x+i][y+i] < 0 and color > 0):
                    possibleMoves.append([x+i,y+i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x-i in range(0,8) and y+i in range(0,8):
                if board[x-i][y+i] == 0:
                    possibleMoves.append([x-i,y+i,False])
                elif (board[x-i][y+i] > 0 and color < 0) or (board[x-i][y+i] < 0 and color > 0):
                    possibleMoves.append([x-i,y+i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x+i in range(0,8) and y-i in range(0,8):
                if board[x+i][y-i] == 0:
                    possibleMoves.append([x+i,y-i,False])
                elif (board[x+i][y-i] > 0 and color < 0) or (board[x+i][y-i] < 0 and color > 0):
                    possibleMoves.append([x+i,y-i,True])
                    break
                else:
                    break

    elif abs(name) == 4:
        #Rook
        for i in range(1,8):
            if x+i in range(0,8):
                if board[x+i][y] == 0:
                    possibleMoves.append([x+i,y,False])
                elif (board[x+i][y] > 0 and color < 0) or (board[x+i][y] < 0 and color > 0):
                    possibleMoves.append([x+i,y,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x-i in range(0,8):
                if board[x-i][y] == 0:
                    possibleMoves.append([x-i,y,False])
                elif (board[x-i][y] > 0 and color < 0) or (board[x-i][y] < 0 and color > 0):
                    possibleMoves.append([x-i,y,True])
                    break
                else:
                    break

        for i in range(1,8):
            if y+i in range(0,8):
                if board[x][y+i] == 0:
                    possibleMoves.append([x,y+i,False])
                elif (board[x][y+i] > 0 and color < 0) or (board[x][y+i] < 0 and color > 0):
                    possibleMoves.append([x,y+i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if y-i in range(0,8):
                if board[x][y-i] == 0:
                    possibleMoves.append([x,y-i,False])
                elif (board[x][y-i] > 0 and color < 0) or (board[x][y-i] < 0 and color > 0):
                    possibleMoves.append([x,y-i,True])
                    break
                else:
                    break

    elif abs(name) == 3:
        #Bishop
        for i in range(1,8):
            if x-i in range(0,8) and y-i in range(0,8):
                if board[x-i][y-i] == 0:
                    possibleMoves.append([x-i,y-i,False])
                elif (board[x-i][y-i] > 0 and color < 0) or (board[x-i][y-i] < 0 and color > 0):
                    possibleMoves.append([x-i,y-i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x+i in range(0,8) and y+i in range(0,8):
                if board[x+i][y+i] == 0:
                    possibleMoves.append([x+i,y+i,False])
                elif (board[x+i][y+i] > 0 and color < 0) or (board[x+i][y+i] < 0 and color > 0):
                    possibleMoves.append([x+i,y+i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x-i in range(0,8) and y+i in range(0,8):
                if board[x-i][y+i] == 0:
                    possibleMoves.append([x-i,y+i,False])
                elif (board[x-i][y+i] > 0 and color < 0) or (board[x-i][y+i] < 0 and color > 0):
                    possibleMoves.append([x-i,y+i,True])
                    break
                else:
                    break

        for i in range(1,8):
            if x+i in range(0,8) and y-i in range(0,8):
                if board[x+i][y-i] == 0:
                    possibleMoves.append([x+i,y-i,False])
                elif (board[x+i][y-i] > 0 and color < 0) or (board[x+i][y-i] < 0 and color > 0):
                    possibleMoves.append([x+i,y-i,True])
                    break
                else:
                    break

    elif abs(name) == 6:
        #King
        if x+1 in range(0,8) and y+1 in range(0,8):
            if board[x+1][y+1] == 0:
                possibleMoves.append([x+1,y+1,False])
            elif (board[x+1][y+1] > 0 and color < 0) or (board[x+1][y+1] < 0 and color > 0):
                possibleMoves.append([x+1,y+1,True])
        if x+1 in range(0,8) and y-1 in range(0,8):
            if board[x+1][y-1] == 0:
                possibleMoves.append([x+1,y-1,False])
            elif (board[x+1][y-1] > 0 and color < 0) or (board[x+1][y-1] < 0 and color > 0):
                possibleMoves.append([x+1,y-1,True])
        if x-1 in range(0,8) and y+1 in range(0,8):
            if board[x-1][y+1] == 0:
                possibleMoves.append([x-1,y+1,False])
            elif (board[x-1][y+1] > 0 and color < 0) or (board[x-1][y+1] < 0 and color > 0):
                possibleMoves.append([x-1,y+1,True])
        if x-1 in range(0,8) and y-1 in range(0,8):
            if board[x-1][y-1] == 0:
                possibleMoves.append([x-1,y-1,False])
            elif (board[x-1][y-1] > 0 and color < 0) or (board[x-1][y-1] < 0 and color > 0):
                possibleMoves.append([x-1,y-1,True])

        if x+1 in range(0,8):
            if board[x+1][y] == 0:
                possibleMoves.append([x+1,y,False])
            elif (board[x+1][y] > 0 and color < 0) or (board[x+1][y] < 0 and color > 0):
                possibleMoves.append([x+1,y,True])
        if x-1 in range(0,8):
            if board[x-1][y] == 0:
                possibleMoves.append([x-1,y,False])
            elif (board[x-1][y] > 0 and color < 0) or (board[x-1][y] < 0 and color > 0):
                possibleMoves.append([x-1,y,True])
        if y+1 in range(0,8):
            if board[x][y+1] == 0:
                possibleMoves.append([x,y+1,False])
            elif (board[x][y+1] > 0 and color < 0) or (board[x][y+1] < 0 and color > 0):
                possibleMoves.append([x,y+1,True])
        if y-1 in range(0,8):
            if board[x][y-1] == 0:
                possibleMoves.append([x,y-1,False])
            elif (board[x][y-1] > 0 and color < 0) or (board[x][y-1] < 0 and color > 0):
                possibleMoves.append([x,y-1,True])


    if abs(name) == 6:
        #print(castleData)
        if name > 0:
            #White King
            #Add Castle
            if castleData[0] == False:
                #King Hasn't Moved
                if board[1][7] == 0 and board[2][7] == 0 and board[3][7] == 0 and castleData[1] == False:
                    #No in between pieces and rook left rook hasn't moved
                    possibleMoves.append([2,7,False])
                if board[5][7] == 0 and board[6][7] == 0 and castleData[2] == False:
                    #No in between pieces and rook left rook hasn't moved
                    possibleMoves.append([6,7,False])

        if name < 0:
            #Black King
            #Add Castle
            if castleData[3] == False:
                #King Hasn't Moved
                if board[1][0] == 0 and board[2][0] == 0 and board[3][0] == 0 and castleData[4] == False:
                    #No in between pieces and rook left rook hasn't moved
                    possibleMoves.append([2,0,False])
                if board[5][0] == 0 and board[6][0] == 0 and castleData[5] == False:
                    #No in between pieces and rook left rook hasn't moved
                    possibleMoves.append([6,0,False])

    return possibleMoves



def pieceDraw(name, x, y):
    if name == -1:
        screen.blit(blackPawn, (x*100,y*100))
    elif name == -6:
        screen.blit(blackKing, (x*100,y*100))
    elif name == -5:
        screen.blit(blackQueen, (x*100,y*100))
    elif name == -4:
        screen.blit(blackRook, (x*100,y*100))
    elif name == -2:
        screen.blit(blackKnight, (x*100,y*100))
    elif name == -3:
        screen.blit(blackBishop, (x*100,y*100))
    
    elif name == 1:
        screen.blit(whitePawn, (x*100,y*100))
    elif name == 6:
        screen.blit(whiteKing, (x*100,y*100))
    elif name == 5:
        screen.blit(whiteQueen, (x*100,y*100))
    elif name == 4:
        screen.blit(whiteRook, (x*100,y*100))
    elif name == 2:
        screen.blit(whiteKnight, (x*100,y*100))
    elif name == 3:
        screen.blit(whiteBishop, (x*100,y*100))

def pieceLimit(newBoard, newName, x, y, newPossibleMoves, newCastleData):
    board = newBoard
    name = newName
    possibleMoves = copy.deepcopy(newPossibleMoves)
    castleData = copy.deepcopy(newCastleData)

    deathSpots = []

    if name > 0:
        #Limiting white

        for i in possibleMoves:
            #Duplicate board and do possible move i
            tempBoard = copy.deepcopy(board)

            tempBoard[x][y] = 0
            tempBoard[i[0]][i[1]] = name

            tempCastleData = copy.deepcopy(castleData)

            if name == 6 and tempCastleData[0] == False:
                tempCastleData[0] = True
                data = copy.deepcopy(checkCastle(tempBoard, 1, tempCastleData))
                tempBoard = copy.deepcopy(data[0])
                tempCastleData = copy.deepcopy(data[1])

            if name == 6:
                #White King Moved
                tempCastleData[0] = True
            if name == 4 and x == 0 and y == 7:
                #White Left Rook Moved
                tempCastleData[1] = True
            if name == 4 and x == 7 and y == 7:
                #White Right Rook Moved
                tempCastleData[2] = True


            for a in range(len(tempBoard)):
                for b in range(len(tempBoard[a])):
                    if tempBoard[a][b] < 0:
                        tempPossibleMoves = copy.deepcopy(findMoves(tempBoard, tempBoard[a][b], a, b, castleData))

                        for k in tempPossibleMoves:
                            if k[0] == i[0] and k[1] == i[1] and k[2] == True:
                                deathSpots.append(k[:2])

    elif name < 0:
        #Limiting black
        
        for i in possibleMoves:
            tempBoard = copy.deepcopy(board)

            tempBoard[x][y] = 0
            tempBoard[i[0]][i[1]] = name

            tempCastleData = copy.deepcopy(castleData)

            if name == -6 and castleData[3] == False:
                tempCastleData[3] = True
                data = copy.deepcopy(checkCastle(tempBoard, -1, tempCastleData))
                tempBoard = copy.deepcopy(data[0])
                tempCastleData = copy.deepcopy(data[1])
            
            if name == -6:
                #Black King Moved
                tempCastleData[3] = True
            if name == -4 and x == 0 and y == 0:
                #Black Left Rook Moved
                tempCastleData[4] = True
            if name == -4 and x == 7 and y == 0:
                #Black Right Rook Moved
                tempCastleData[5] = True

            for a in range(len(tempBoard)):
                for b in range(len(tempBoard[a])):
                    if board[a][b] > 0:
                        tempPossibleMoves = copy.deepcopy(findMoves(tempBoard, tempBoard[a][b], a, b, castleData))

                        for k in tempPossibleMoves:
                            if k[0] == i[0] and k[1] == i[1] and k[2] == True:
                                deathSpots.append(k[:2])

    newDeathSpots = []
    for i in deathSpots:
        if i not in newDeathSpots:
            newDeathSpots.append(i)
        
    updatedPossibleMoves = []
    for i in possibleMoves:
        if [i[0],i[1]] not in newDeathSpots:
            updatedPossibleMoves.append(i)

    return updatedPossibleMoves


def checkLimit(newBoard, newName, x, y, newPossibleMoves, newCastleData):
    board = copy.deepcopy(newBoard)
    possibleMoves = copy.deepcopy(newPossibleMoves)
    name = newName
    castleData = copy.deepcopy(newCastleData)

    notSpots = []

    if name > 0:
        for i in possibleMoves:
            tempBoard = copy.deepcopy(board)

            tempBoard[x][y] = 0
            tempBoard[i[0]][i[1]] = name

            tempCastleData = copy.deepcopy(castleData)

            if name == 6 and tempCastleData[0] == False:
                tempCastleData[0] = True
                data = copy.deepcopy(checkCastle(tempBoard, 1, tempCastleData))
                tempBoard = copy.deepcopy(data[0])
                tempCastleData = copy.deepcopy(data[1])

            if name == 6:
                #White King Moved
                tempCastleData[0] = True
            if name == 4 and x == 0 and y == 7:
                #White Left Rook Moved
                tempCastleData[1] = True
            if name == 4 and x == 7 and y == 7:
                #White Right Rook Moved
                tempCastleData[2] = True

            
            checkData = checkCheck(tempBoard, tempCastleData)

            if checkData == 1:
                notSpots.append(copy.deepcopy(i))

    if name < 0:
        for i in possibleMoves:
            tempBoard = copy.deepcopy(board)

            tempBoard[x][y] = 0
            tempBoard[i[0]][i[1]] = name

            tempCastleData = copy.deepcopy(castleData)

            if name == -6 and castleData[3] == False:
                tempCastleData[3] = True
                data = copy.deepcopy(checkCastle(tempBoard, -1, tempCastleData))
                tempBoard = copy.deepcopy(data[0])
                tempCastleData = copy.deepcopy(data[1])
            
            if name == -6:
                #Black King Moved
                tempCastleData[3] = True
            if name == -4 and x == 0 and y == 0:
                #Black Left Rook Moved
                tempCastleData[4] = True
            if name == -4 and x == 7 and y == 0:
                #Black Right Rook Moved
                tempCastleData[5] = True
            
            checkData = checkCheck(tempBoard, tempCastleData)

            if checkData == -1:
                notSpots.append(copy.deepcopy(i))
    
    newNotSpots = []
    for i in notSpots:
        if i not in newNotSpots:
            newNotSpots.append(i[:2])

    updatedPossibleMoves = []
    for i in possibleMoves:
        if [i[0],i[1]] not in newNotSpots:
            updatedPossibleMoves.append(i)

    return updatedPossibleMoves


def checkCastle(newBoard, newTurn, newCastleData):
    #First time king has moved, we check and execute the castle
    board = copy.deepcopy(newBoard)
    turn = newTurn
    castleData = copy.deepcopy(newCastleData)

    if turn == 1:
        if board[2][7] == 6:
            #Castle to left made
            board[0][7] = 0
            board[3][7] = 4
            castleData[1] = True

        if board[6][7] == 6:
            #Castle to Right made
            board[7][7] = 0
            board[5][7] = 4
            castleData[2] = True

    if turn == -1:
        if board[2][0] == -6:
            #Castle to left made
            board[0][0] = 0
            board[3][0] = -4
            castleData[3] = True

        if board[6][0] == -6:
            #Castle to Right made
            board[7][0] = 0
            board[5][0] = -4
            castleData[4] = True

    return [board, castleData]


def checkmateCheck(board, castleData):
    checkData = checkCheck(board, castleData)
    if checkData != 0:
        whiteKingPos = []
        blackKingPos = []
        '''
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 6:
                    whiteKingPos = [i,j]
                if board[i][j] == -6:
                    blackKingPos = [i,j]
        '''
        if checkData == 1:
            #If white in check
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] > 0:
                        currentMoves = copy.deepcopy(findMoves(board, board[i][j], i, j, castleData))
                        currentMoves = copy.deepcopy(checkLimit(board, board[i][j], i, j, currentMoves, castleData))
                        if len(currentMoves) > 0:
                            return 0
            return 1

        if checkData == -1:
            #If black in check
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] < 0:
                        currentMoves = copy.deepcopy(findMoves(board, board[i][j], i, j, castleData))
                        currentMoves = copy.deepcopy(checkLimit(board, board[i][j], i, j, currentMoves, castleData))
                        if len(currentMoves) > 0:
                            return 0
            return -1

    return 0




def checkCheck(board, castleData):
    #Returns who is in check, -1 Black, 1 White, 0 None

    whiteKingPos = []
    blackKingPos = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 6:
                whiteKingPos = [i,j]
            if board[i][j] == -6:
                blackKingPos = [i,j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                #Finds white moves
                currentMoves = copy.deepcopy(findMoves(board, board[i][j], i, j, castleData))
                if board[i][j] == 6:
                    currentMoves = copy.deepcopy(pieceLimit(board, board[i][j], i, j, currentMoves, castleData))
                for k in currentMoves:
                    if k[0] == blackKingPos[0] and k[1] == blackKingPos[1]:
                        return -1
                    '''
                    try:
                        if k[0] == blackKingPos[0] and k[1] == blackKingPos[1]:
                            return -1
                    except:
                        print("ERROR")
                        print(k, blackKingPos)

                        for p in board:
                            print(p)
                        print()
                    '''

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] < 0:
                #Finds black moves
                currentMoves = copy.deepcopy(findMoves(board, board[i][j], i, j, castleData))
                if board[i][j] == -6:
                    currentMoves = copy.deepcopy(pieceLimit(board, board[i][j], i, j, currentMoves, castleData))
                for k in currentMoves:
                    if k[0] == whiteKingPos[0] and k[1] == whiteKingPos[1]:
                        return 1
                    '''
                    try:
                        if k[0] == whiteKingPos[0] and k[1] == whiteKingPos[1]:
                            return 1
                    except:
                        print("ERROR")
                        print(k, whiteKingPos)

                        for p in board:
                            print(p)
                        print()
                    '''

    return 0

def choosePosition(pos, newBoard, newSelectedPiece, newTurn, newPossibleMoves, newInCheck, newCastleData):
    x = -1
    y = -1
    for i in range(0,8):
        if pos[0] in range(i*100, i*100 + 100):
            x = i
        if pos[1] in range(i*100, i*100 + 100):
            y = i

    board = copy.deepcopy(newBoard)
    selectedPiece = copy.deepcopy(newSelectedPiece)
    turn = newTurn
    possibleMoves = copy.deepcopy(newPossibleMoves)
    inCheck = newInCheck
    castleData = copy.deepcopy(newCastleData)

    #'''
    if turn == 1:
        #White Move
        if selectedPiece == []:
            if board[x][y] > 0:
                selectedPiece = [x,y]
                possibleMoves = findMoves(board, board[x][y], x, y, newCastleData)
            if board[x][y] == 6:
                possibleMoves = copy.deepcopy(pieceLimit(board, board[x][y], x, y,possibleMoves, castleData))
            possibleMoves = copy.deepcopy(checkLimit(board, board[x][y], x, y, possibleMoves, castleData))

        else:
            if [x,y] == selectedPiece or ([x,y,False] not in possibleMoves and [x,y,True] not in possibleMoves):
                 #Unselect Piece
                selectedPiece = []
                possibleMoves = []
            
            elif [x,y,False] in possibleMoves or [x,y,True] in possibleMoves:
                #Move Piece
                pieceName = board[selectedPiece[0]][selectedPiece[1]]

                board[x][y] = pieceName
                board[selectedPiece[0]][selectedPiece[1]] = 0


                if pieceName == 6 and castleData[0] == False:
                    castleData[0] = True
                    data = copy.deepcopy(checkCastle(board, turn, castleData))
                    board = copy.deepcopy(data[0])
                    castleData = copy.deepcopy(data[1])

                if pieceName == 6:
                    #White King Moved
                    castleData[0] = True
                if pieceName == 4 and selectedPiece[0] == 0 and selectedPiece[1] == 7:
                    #White Left Rook Moved
                    castleData[1] = True
                if pieceName == 4 and selectedPiece[0] == 7 and selectedPiece[1] == 7:
                    #White Right Rook Moved
                    castleData[2] = True

                turn = turn*-1
                selectedPiece = []
                possibleMoves = []

                inCheck = checkCheck(board, castleData)
                if checkmateCheck(board, castleData) != 0:
                    print("Checkmate")
    #'''

    #'''
    if turn == -1:
        #Black Move
        if selectedPiece == []:
            if board[x][y] < 0:
                selectedPiece = [x,y]
                possibleMoves = findMoves(board, board[x][y], x, y, newCastleData)
            if board[x][y] == -6:
                possibleMoves = copy.deepcopy(pieceLimit(board, board[x][y], x, y,possibleMoves, castleData))
            
            possibleMoves = copy.deepcopy(checkLimit(board, board[x][y], x, y, possibleMoves, castleData))

        else:
            if [x,y] == selectedPiece or ([x,y,False] not in possibleMoves and [x,y,True] not in possibleMoves):
                #Unselect Piece
                selectedPiece = []
                possibleMoves = []
            
            elif [x,y,False] in possibleMoves or [x,y,True] in possibleMoves:
                #Move Piece
                pieceName = board[selectedPiece[0]][selectedPiece[1]]

                board[x][y] = pieceName
                board[selectedPiece[0]][selectedPiece[1]] = 0

                if pieceName == -6 and castleData[3] == False:
                    castleData[3] = True
                    data = copy.deepcopy(checkCastle(board, turn, castleData))
                    board = copy.deepcopy(data[0])
                    castleData = copy.deepcopy(data[1])

                if pieceName == -6:
                    #Black King Moved
                    castleData[3] = True
                if pieceName == -4 and selectedPiece[0] == 0 and selectedPiece[1] == 0:
                    #Black Left Rook Moved
                    castleData[4] = True
                if pieceName == -4 and selectedPiece[0] == 7 and selectedPiece[1] == 0:
                    #Black Right Rook Moved
                    castleData[5] = True

                turn = turn*-1
                selectedPiece = []
                possibleMoves = []

                inCheck = checkCheck(board, castleData)

                if checkmateCheck(board, castleData) != 0:
                    print("Checkmate")
    #'''

    return [board, selectedPiece, turn, possibleMoves, inCheck, castleData]


def inGame():
    '''
    1 = pawn
    2 = knight
    3 = bishop
    4 = rook
    5 = queen
    6 = king
    - = black
    + = white
    '''

    board = [
        [-4,-1,0,0,0,0,1,4],
        [-2,-1,0,0,0,0,1,2],
        [-3,-1,0,0,0,0,1,3],
        [-5,-1,0,0,0,0,1,5],
        [-6,-1,0,0,0,0,1,6],
        [-3,-1,0,0,0,0,1,3],
        [-2,-1,0,0,0,0,1,2],
        [-4,-1,0,0,0,0,1,4]
    ]

    selectedPiece = []
    turn = 1 #White starts
    possibleMoves = []
    inCheck = 0 #-1 means black in Check, 1 means white in Check
    castleData = [False, False, False, False, False, False] #White King, White Rook Left, White Rook Right, Black King, Black Rook Left, Black Rook Right

    while True:
        
        
        if turn == 1:
            #AI Moves
            minimaxData = copy.deepcopy(minimax(board, turn, castleData, 3, float('-inf'), float('inf')))
            print(minimaxData[0])
            board = copy.deepcopy(minimaxData[1])
            castleData = copy.deepcopy(minimaxData[2])
            turn = turn*-1
            inCheck = checkCheck(board, castleData)

            checkmateData = checkmateCheck(board, castleData)

            if checkmateData != 0:
                print("Checkmate")
        

        '''
        if turn == -1:
            #AI Moves
            minimaxData = copy.deepcopy(minimax(board, turn, castleData, 2, float('-inf'), float('inf')))
            print(minimaxData[0])
            board = copy.deepcopy(minimaxData[1])
            castleData = copy.deepcopy(minimaxData[2])
            turn = turn*-1
            inCheck = checkCheck(board, castleData)

            checkmateData = checkmateCheck(board, castleData)

            if checkmateData != 0:
                print("Checkmate")
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                #'''
                data = copy.deepcopy(choosePosition(pygame.mouse.get_pos(), board, selectedPiece, turn, possibleMoves, inCheck, castleData))

                board = copy.deepcopy(data[0])
                selectedPiece = copy.deepcopy(data[1])
                turn = copy.deepcopy(data[2])
                possibleMoves = copy.deepcopy(data[3])
                inCheck = copy.deepcopy(data[4])
                castleData = copy.deepcopy(data[5])
                #'''

        screen.fill((0, 0, 0))

        for i in range(0,8,2):
            for j in range(0,8,2):
                pygame.draw.rect(screen, LIGHTGREEN, (i*100,j*100,100,100))
        for i in range(1,9,2):
            for j in range(1,9,2):
                pygame.draw.rect(screen, LIGHTGREEN, (i*100,j*100,100,100))

        for i in range(0,8,2):
            for j in range(0,8,2):
                pygame.draw.rect(screen, DARKGREEN, (i*100+100,j*100,100,100))
        for i in range(1,9,2):
            for j in range(1,9,2):
                pygame.draw.rect(screen, DARKGREEN, (i*100-100,j*100,100,100))

        for i in range(8):
            for j in range(8):
                pieceDraw(board[i][j], i, j)

        if selectedPiece != []:
            for i in possibleMoves:
                if i[2] == False:
                    pygame.draw.rect(screen, BLUE, (i[0]*100, i[1]*100, 100, 100), 3)
                else:
                    pygame.draw.rect(screen, RED, (i[0]*100, i[1]*100, 100, 100), 3)

            pygame.draw.rect(screen, BLACK, (selectedPiece[0]*100, selectedPiece[1]*100, 100, 100), 3)

        pygame.display.flip()
        fpsClock.tick(fps)


inGame()