import sys
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

#productNames to Store the Name of Products
productNames=[]

#columnValues to store Values of Table Row Wise
rowValues=[]

#zEquation to contain Z row Coefficients
zEquation=[]

#solutions to store the Index Value of the Table
solutions=[]

#variable Name
x='X'

#Used to get The Objective
def getObjective():    
    objective=input('\n(Press Ctrl+C to Terminate)\n1.Maximization \n2.Minimization \nWhat Do you Want to Do ?<1/2>==>')
    if objective=='1':
        return objective
    elif objective=='2':
        return objective
    else:
        print('Enter Valid Option!')
        return 0

#Used to Find Corner Points and Plot The Graph
def constraintPlot(rowValues):
    plotListX1=[]
    plotListX2=[]
    maximum=[]
    PlotSet=set()
    evaluateCornerPoint=set()
    constraintFlag=[]

    for row in rowValues:
        maximum.append(row[2])

    for row in rowValues:
        #x1=0 find x2 & x2=0 find x1
        if row[0] !=0 and row[1] !=0 and row[2]!=0:
            x1=[0,row[2]/row[0]]
            x2=[row[2]/row[1],0]
            plotListX1.append(x1)
            plotListX2.append(x2)
            PlotSet.add((x1[0],x2[0]))
            PlotSet.add((x1[1],x2[1]))
        #if RHS=0 then Substitue Value un Equation and Get Points 
        elif row[2]==0:
            x=np.linspace(0,max(maximum))
            y=row[0]*x/(-1*row[1])
            plt.plot(x,y)
        #if x=a,y=0 or x=0,y=a
        else:
            if row[0]==0:
                plt.axhline(y=row[2])
                PlotSet.add((row[0],row[2]))
            elif row[1]==0:
                plt.axvline(x=row[2])
                PlotSet.add((row[2],row[1]))
    #Plot the Points
    for i in range(len(plotListX1)):
        plt.plot(plotListX1[i],plotListX2[i])
    #Used to Solve Equations
    x,y=symbols('x y')

    cornerSet=set()

    intersectFlag=True

    for eq1 in rowValues:
        for eq2 in rowValues:
            if eq1!=eq2:
                #if Intesection Exists
                Equation1=Eq(eq1[0]*x+eq1[1]*y,eq1[2])
                Equation2=Eq(eq2[0]*x+eq2[1]*y,eq2[2])
                solutionDict=solve((Equation1,Equation2),(x,y))

                #if Intersectin Doesnt Exist
                if not solutionDict:
                    intersectFlag=False
                    break
                #Adding Points to Set
                if solutionDict[x]>0 and solutionDict[y]>0:
                    cornerSet.add((solutionDict[x],solutionDict[y]))

        #if Intersectin Doesnt Exist            
        if intersectFlag==False:
            break
    #if Intersectin Doesnt Exist
    if intersectFlag==False:
        for Point in PlotSet:
            plt.plot(Point[0],Point[1])
        for Point in PlotSet:
            plt.scatter(Point[0],Point[1])
        plt.savefig('Answer.png')
        plt.show()
        return PlotSet
    else:
        #Find Points that Satisfy all the Constraints
        for Point in cornerSet:
            for constraint in rowValues:
                value=Point[0]*constraint[0]+Point[1]*constraint[1]
                if constraint[3]=='<=':
                    if value<=constraint[2]:
                        constraintFlag.append(1)
                    else:
                        constraintFlag.append(0)
                elif constraint[3]=='>=':
                    if value>=constraint[2]:
                        constraintFlag.append(1)
                    else:
                        constraintFlag.append(0)
                elif constraint[3]=='=':
                    if value==constraint[2]:
                        constraintFlag.append(1)
                    else:
                        constraintFlag.append(0)
            if 0 not in constraintFlag:    
                evaluateCornerPoint.add(Point)
            constraintFlag.clear()
        for Point in evaluateCornerPoint:
            plt.scatter(Point[0],Point[1])
        plt.savefig('Answer.png')
        plt.show()
        if len(evaluateCornerPoint)==0:
            print('There are No Points that satisfy all Constraints of the Problem')
            sys.exit()
        return evaluateCornerPoint

Flag=1
while Flag:
    getObjectiveStatus=getObjective()
    if getObjectiveStatus=='1' or getObjectiveStatus=='2':
        Flag=False
global constraintNumber,productNumber
global constraintNames
productNumber=int(input('Enter The Number Of Products :'))
constraintNumber=int(input('Enter The Number of Constraints :'))
constraintNames=[x+str(i) for i in range(1,productNumber+1)]

for i in range(1,constraintNumber+1):
    productNames.append(input(f'Enter Product-{i} Name :'))

for i in constraintNames:
    while True:
        try:
            value=float(Fraction(input(f'Enter the Value of {str(i)} in Z-Equation :')))
            break
        except ValueError:
            print('Enter a Valid Value!')
    zEquation.append(value)
for product in productNames:
    for constraint in constraintNames:
        while True:
            try:
                value=float(Fraction(input(f'Enter the Value of {constraint} in {product} :')))
                break
            except ValueError:
                print('Enter a Valid Value!')
        rowValues.append(value)
    rowValues.append(float(Fraction(input(f'Enter RHS of {product} :'))))
    rowValues.append(input('Enter "<=" or ">=" or "=" :'))
rowValues=[rowValues[i:i+ productNumber +2] for i in range(0,len(rowValues), productNumber +2)]

evaluateCornerPoint=constraintPlot(rowValues)
evaluateCornerPoint=list(evaluateCornerPoint)

if len(evaluateCornerPoint)>=1:
    answer=[]
    for Point in evaluateCornerPoint:
        value=zEquation[0]*Point[0]+zEquation[1]*Point[1]
        answer.append(value)
    if getObjectiveStatus=='1':
        print(f'Optimal Value :{max(answer)}')
        index=answer.index(max(answer))
        Point=evaluateCornerPoint[index]
        print(f'X1 = {Point[0]}')
        print(f'X2 = {Point[1]}')
    elif getObjectiveStatus=='2':
        if min(answer)!=0:
            print(f'Optimal Value :{min(answer)}')
            index=answer.index(min(answer))
            Point=evaluateCornerPoint[index]
            print(f'X1 = {Point[0]}')
            print(f'X2 = {Point[1]}')
        elif len(answer)>1 and min(answer)==0:
            index=answer.index(min(answer))
            del answer[index:index+1]
            del evaluateCornerPoint[index:index+1]
            print(f'Optimal Value :{min(answer)}')
            index=answer.index(min(answer))
            Point=evaluateCornerPoint[index]
            print(f'X1 = {Point[0]}')
            print(f'X2 = {Point[1]}')
        elif len(answer)==1 and min(answer)==0:
            value=zEquation[0]*Point[0]+zEquation[1]*Point[1]
            print(f'Optimal Value :{value}')
            print(f'X1 = {Point[0]}')
            print(f'X2 = {Point[1]}')
else:
    print('Solution Doesnt Exist')
    print('There Should be more Constraints or Analyst should Decide the Solution')
