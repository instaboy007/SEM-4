from typing import final
import numpy as np
from fractions import Fraction
import pandas as pd
from pandas.core.construction import array
import sys

#productNames to Store the Name of Products
productNames=[]

#columnValues to store Values of Table Row Wise
rowValues=[]

#zEquation to contain Z row Coefficients
zEquation=[]

#ZEquation to contain A-Row Coefficients
ZEquation=[]

#solutions to store the Index Value of the Table
solutions=[]

#variable Name
x='X'

#removableVariables is used to store Artificial  Variables
removableVariables=[]

#getObjective Function is used to choose Maximization or Minimization Enter 1 to Maximize and 2 to Minimize 
def getObjective():    
    objective=input('\n(Press Ctrl+C to Terminate)\n1.Maximization \n2.Minimization \nWhat Do you Want to Do ?<1/2>==>')
    if objective=='1':
        return objective
    elif objective=='2':
        return objective
    else:
        print('Enter Valid Option!')
        return 0

#standardizeRowMax is used to Standardize the Constraints( ! Works only for Maximization Problems)
def standardizeRowsMax(rowValues):

    #finalRow is List of Lists which contains the Coefficients of Constraints
    finalrow=[rowValues[i:i+ productNumber +1] for i in range(0,len(rowValues), productNumber +1)]

    #For each Row 0 is added in the Last
    for row in finalrow:
        while len(row)<(constraintNumber+productNumber):
            row.insert(-1,0)
    
    #For Each Row 1 is inserted in Slack Variable Position
    i=productNumber
    for row in finalrow:
        row.insert(i,1)
        i+=1
    
    #final Row is Returned
    return finalrow

#standardizeRowsMin is used to Standardize Constraints(! Works only for Maximization Problems)
def standardizeRowsMin(rowValues):

    #finalRow is a List of Lists which contains the Coefficients of Constraints
    finalrow=[rowValues[i:i+ productNumber +1] for i in range(0,len(rowValues), productNumber +1)]

    #sumZ is used to store A-Row Values
    sumZ=(0-np.array(finalrow).sum(axis=0)).tolist()

    #Values in sumZ is Copied to ZEquation which is actually A-Row
    for i in sumZ:
        ZEquation.append(i)

    #zeros are inserted in finalRow at Last    
    for row in finalrow:
        while len(row)<(2*constraintNumber+productNumber-1):
            row.insert(-1,0)

    #-1 is inserted at indices where Surplus Variables are introduced and 1 is insered in A-Row at Surplus Variable indices       
    i=productNumber
    for row in finalrow:
        row.insert(i,-1)
        ZEquation.insert(-1,1)
        i+=1
    
    #1 is inserted at Artificial Variable Indices
    for row in finalrow:
        row.insert(i,1)
        i+=1
    
    #0 is inserted in A-Row at Artificial Variable indices
    while len(ZEquation)<len(finalrow[0]):
        ZEquation.insert(-1,0)

    #finalrow is Returned
    return finalrow

#Iterate functionn is used to Perform the Iterations
def Iterate(rowValues,columnValues):

    #Initially Iteration is Set to 1
    iteration=1

    #zRow contains the Z-Row
    zRow=rowValues[0]

    #zRowMin contains The Most Negative Co-Efficient in the Z-Row
    zRowMin=min(zRow[:-1])

    #minFlag is set to 1
    minFlag=1

    #pivotElement is set to 2 so the While Loop Condition Gets Satisfied
    pivotElement=2

    #While Loop Ends When Z-Row has All Positive Values
    while zRowMin< 0 < pivotElement !=1 and minFlag==1:

        #zRow has The Z-Row
        zRow=rowValues[0]

        #rhsColumn has the RHS Column
        rhsColumn=columnValues[-1]

        #zRowMin has the Most Negative Co-Efficient in Z-Row(-1 is to Leave RHS Column in Z-Row)
        zRowMin=min(zRow[:-1])

        #zRowMinIndex has the Index of The Most Negative Coefficient in Z-Row(This Index Value Column Enters The Basis)
        zRowMinIndex=zRow.index(zRowMin)

        #pivotColum will be The Column where Most Negative Coefficient is Present 
        pivotColumn=columnValues[zRowMinIndex]

        #pivotColumnIndex is Found
        pivotColumnIndex=columnValues.index(pivotColumn)

        #BrCRRatio is a List Which is used to Store The Br/Cr Values
        BrCRRatio=[]

        #Calculating Br/Cr Ratio and Storing it in BrCrRatio
        i=1
        for _ in rhsColumn[1:]:
            try:
                value=float(rhsColumn[i]/pivotColumn[i])

                #If Br/Cr < 0 Then a Big Value 0f 1000000000 is Appended to The List 
                # So we Can Choose The Minimum Positive Br/Cr Value from The Rest
                if value<0:
                    value=1000000000
                BrCRRatio.append(value)
            except ZeroDivisionError:

                #In Br/Cr if Cr is 0 the 1000000000 is Appended So we Can Choose
                # The Minimum Positive Br/Cr Value from The Rest
                value=1000000000
                BrCRRatio.append(value)
            i+=1
        
        #minBrCrRatio has the Minimum Br/Cr Value
        minBrCRRatio=min(BrCRRatio)

        #minBrCRRatioIndex has the Index of the Minimum Br/Cr Value
        minBrCRRatioIndex=BrCRRatio.index(minBrCRRatio)+1

        #pivotElement will be at the minBrCrRatioIndex in pivotColumn
        pivotElement=pivotColumn[minBrCRRatioIndex]

        #pivotRow will be at the minBrCrRatioIndex in rowValues
        pivotRow=rowValues[minBrCRRatioIndex]

        #pivotRowIndex will Have The index of PivotRow
        pivotRowIndex=rowValues.index(pivotRow)

        #For Loop to Determine The New Rows
        for row in rowValues:

            #For Rows Other Than PivotRow and Z-Row
            if row is not pivotRow and row is not rowValues[0]:

                #Divide Values in PivotColumn by Pivot Element to find Value 
                value=row[zRowMinIndex]/pivotElement

                #Multiply Value to PivotRow
                rowValue=np.array(pivotRow)*value

                #Subtract row and RowValue Now we'll get 0 in Pivot Column
                newRow=(np.round((np.array(row)-rowValue),decimals)).tolist()

                #oldRow is Replaced With New Row
                rowValues[rowValues.index(row)]=newRow

            #If row is pivotRow    
            elif row is pivotRow:

                #Divide Row Elements by PivotElement
                newRow=(np.round((np.array(row)/pivotElement),decimals)).tolist()

                #Replacing OldPivot Row by New Pivot Row
                rowValues[rowValues.index(row)]=newRow

            #row is Z-Row    
            else:

                #Divide Values in PivotColumn by Pivot Element to find Value 
                value=abs(row[zRowMinIndex])/pivotElement

                 #Multiply Value to PivotRow
                rowValue=np.array(pivotRow)*value

                #Subtract row and RowValue Now we'll get 0 in Pivot Column
                newRow=(np.round((np.array(row)+rowValue),decimals)).tolist()

                #oldRow is Replaced With New Row
                rowValues[rowValues.index(row)]=newRow
        
        #columnValues is Emptied 
        columnValues[:]=[]

        #columnValues are Inserted By Transposing RowValues
        columnValues=columnValues+np.array(rowValues).T.tolist()

        #if minBrCrRatio is 1000000000 then minFlag is set to 0 else 1
        if min(BrCRRatio)!=1000000000:
            minFlag=1
        else:
            minFlag=0

        #Printing pivotlement,Entering and Leaving Variable
        print('-----------------------------------------------------------')
        print(f'\nPivot Element :{pivotElement}')
        print(f'Entering Variable :{constraintNames[zRowMinIndex]}')
        print(f'Leaving Variable :{solutions[pivotRowIndex]}')

        #Appending Entering Variable Name in Basic Variable Column
        solutions[pivotRowIndex]=constraintNames[pivotColumnIndex]

        #Printing Table
        print(f'\nIteraion -{iteration}')
        table=pd.DataFrame(np.array(rowValues),columns=constraintNames,index=solutions)
        print(table)

        #iteration value is Increamented
        iteration+=1

        #zRow is Updated
        zRow=rowValues[0]

        #rhsColumn is Updated
        rhsColumn=columnValues[-1]

        #zRowMin and its Index is Found
        zRowMin=min(zRow[:-1])
        zRowMinIndex=zRow.index(zRowMin)

        #pivotColumn is Found
        pivotColumn=columnValues[zRowMinIndex]

        #BrCrRatio is Emptied
        BrCRRatio=[]

        #Loop to Find Br/Cr Values
        i=1
        for _ in rhsColumn[1:]:
            try:
                value=float(rhsColumn[i]/pivotColumn[i])
                if value<=0:
                    value=1000000000
                BrCRRatio.append(value)
            except ZeroDivisionError:
                value=1000000000
                BrCRRatio.append(value)
            i+=1

        #minBrCrRatio ,its Index and pivotElement are Found
        minBrCRRatio=min(BrCRRatio)
        minBrCRRatioIndex=BrCRRatio.index(minBrCRRatio)+1
        pivotElement=pivotColumn[minBrCRRatioIndex]

        #If Pivot Element is 0 then Solution Doesnt Exist
        if pivotElement<0:
            print('\nNo Solution!')
            sys.exit(0)

    #Printing Final Optimal Solution
    print('\n')
    Answer=[]
    j=0
    for i in rhsColumn:
        if solutions[j] in basicVariable:
            Answer.append(f'{solutions[j]} = {i}')
        j+=1
    for i in Answer:
        print(i)
    print(f'Get Maximum Benefit of {rhsColumn[0]}')


def IterateMin(columnValues,rowValues):
    iteration=1
    zRow=columnValues[1]
    zRowMin=min(zRow[:-1])
    minFlag=1
    pivotElement=2
    while zRowMin < 0 < pivotElement and minFlag==1:
        zRow=columnValues[1]
        rhsColumn=rowValues[-1]
        zRowMin=min(zRow[:-1])
        zRowMinIndex=zRow.index(zRowMin)
        pivotColumn=rowValues[zRowMinIndex]
        pivotColumnIndex=rowValues.index(pivotColumn)
        BrCRRatio=[]
        i=2
        for _ in rhsColumn[2:]:
            try:
                value=float(rhsColumn[i]/pivotColumn[i])
                if value<0:
                    value=1000000000
                BrCRRatio.append(value)
            except ZeroDivisionError:
                value=1000000000
                BrCRRatio.append(value)
            i+=1
        minBrCRRatio=min(BrCRRatio)
        minBrCRRatioIndex=BrCRRatio.index(minBrCRRatio)+2
        pivotElement=pivotColumn[minBrCRRatioIndex]
        pivotRow=columnValues[minBrCRRatioIndex]
        pivotRowIndex=columnValues.index(pivotRow)
        for row in columnValues:
            if row is not pivotRow and row is not columnValues[1]:
                value=row[zRowMinIndex]/pivotElement
                rowValue=np.array(pivotRow)*value
                newRow=(np.round((np.array(row)-rowValue),decimals)).tolist()
                columnValues[columnValues.index(row)]=newRow
            elif row is pivotRow:
                newRow=(np.round((np.array(row)/pivotElement),decimals)).tolist()
                columnValues[columnValues.index(row)]=newRow
            else:
                value=row[zRowMinIndex]/pivotElement
                rowValue=np.array(pivotRow)*value
                newRow=(np.round((np.array(row)-rowValue),decimals)).tolist()
                columnValues[columnValues.index(row)]=newRow
        rowValues[:]=[]
        rowValues=rowValues+np.array(columnValues).T.tolist()
        if min(BrCRRatio)!=1000000000:
            minFlag=1
        else:
            minFlag=0
        print('-----------------------------------------------------------')
        print(f'\nPivot Element :{pivotElement}')
        print(f'Entering Variable :{constraintNames[zRowMinIndex]}')
        print(f'Leaving Variable :{solutions[pivotRowIndex]}')
        #removable=solutions[pivotRowIndex]
        solutions[pivotRowIndex]=constraintNames[pivotColumnIndex]
        '''if removable in removableVariables:
            removableIndex=constraintNames.index(removable)
            for column in columnValues:
                column.remove(column[removableIndex])
            constraintNames.remove(removable)'''
        print(f'\nIteraion -{iteration}')
        table=pd.DataFrame(np.array(columnValues),columns=constraintNames,index=solutions)
        print(table)
        iteration+=1
        rowValues[:]=[]
        for i in np.array(columnValues).T.tolist():
            rowValues.append(i)
        zRow=columnValues[1]
        rhsColumn=rowValues[-1]
        zRowMin=min(zRow[:-1])
        zRowMinIndex=zRow.index(zRowMin)
        pivotColumn=rowValues[zRowMinIndex]
        BrCRRatio=[]
        i=2
        for _ in rhsColumn[2:]:
            try:
                value=float(rhsColumn[i]/pivotColumn[i])
                if value<=0:
                    value=1000000000
                BrCRRatio.append(value)
            except ZeroDivisionError:
                value=1000000000
                BrCRRatio.append(value)
            i+=1
        minBrCRRatio=min(BrCRRatio)
        minBrCRRatioIndex=BrCRRatio.index(minBrCRRatio)+2
        pivotElement=pivotColumn[minBrCRRatioIndex]
        if pivotElement<0:
            print('\nNo Solution!')
            sys.exit(0)

    print('\n')
    Answer=[]
    j=0
    for i in rhsColumn:
        if solutions[j] in basicVariable:
            Answer.append(f'{solutions[j]} = {i}')
        j+=1
    for i in Answer:
        print(i)
    print(f'Requires Minimum Effort of {rhsColumn[0]*-1}')
        
def Maximize(rowValues,columnValues):
    print('-----------------------------------------------------------')
    print('\nInitial Table')
    table=pd.DataFrame(np.array(rowValues),columns=constraintNames,index=solutions)
    print(table)
    Iterate(rowValues,columnValues)

def Minimize(rowValues,columnValues):
    print('-----------------------------------------------------------')
    print('\nInitial Table')
    table=pd.DataFrame(np.array(rowValues),columns=constraintNames,index=solutions)
    print(table)
    IterateMin(rowValues,columnValues)


Flag=1
while Flag:
    getObjectiveStatus=getObjective()
    if getObjectiveStatus=='1' or getObjectiveStatus=='2':
        Flag=False

global decimals
global constraintNumber, productNumber
global constraintNames
productNumber=int(input('Enter The Number Of Products :'))
constraintNumber=int(input('Enter The Number of Constraints :'))
constraintNames=[x+str(i) for i in range(1,productNumber+1)]
basicVariable=[]
for i in constraintNames:
    basicVariable.append(i)
for i in range(1,constraintNumber+1):
    productNames.append(input(f'Enter Product-{i} Name :'))

if getObjectiveStatus=='1':
    for i in constraintNames:
        while True:
            try:
                value=float(Fraction(input(f'Enter the Value of {str(i)} in Z-Equation :')))
                break
            except ValueError:
                print('Enter a Valid Value!')
        zEquation.append(0-int(value))
    zEquation.append(0)
    while len(zEquation)<=(constraintNumber+productNumber):
        zEquation.append(0)
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
    
    rowValues=standardizeRowsMax(rowValues)
    i=len(constraintNames)+1
    while len(constraintNames)< len(rowValues[0])-1:
        constraintNames.append('X'+str(i))
        solutions.append('X'+str(i))
        i+=1
    solutions.insert(0,'Z')
    constraintNames.append('Solution')
    rowValues.insert(0,zEquation)
    columnValues=np.array(rowValues).T.tolist()
    decimals=3
    Maximize(rowValues,columnValues)
elif getObjectiveStatus=='2':
    for i in constraintNames:
        while True:
            try:
                value=float(Fraction(input(f'Enter the Value of {str(i)} in Z-Equation :')))
                break
            except ValueError:
                print('Enter a Valid Value!')
        zEquation.append(int(value))
    zEquation.append(0)

    while len(zEquation)<=(constraintNumber+productNumber):
        zEquation.append(0)

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
    
    rowValues=standardizeRowsMin(rowValues)
    i=len(constraintNames)+1
    while len(constraintNames)< constraintNumber+productNumber:
        constraintNames.append('X'+str(i))
        solutions.append('X'+str(i))
        i+=1
    solutions.insert(0,'Z')
    solutions[:]=[]
    i=len(constraintNames)+1
    while len(constraintNames)<len(rowValues[0][1:]):
        removableVariables.append('X'+str(i))
        constraintNames.append('X'+str(i))
        i+=1
    removableVariables.insert(0,'Z')
    removableVariables.insert(1,'Z`')
    constraintNames.append('Solution')
    for i in removableVariables:
        solutions.append(i)
    while len(zEquation)<len(rowValues[0]): 
         zEquation.append(0) 
    rowValues.insert(0,zEquation)
    rowValues.insert(1,ZEquation)
    columnValues=np.array(rowValues).T.tolist()
    decimals=3
    Minimize(rowValues,columnValues)



