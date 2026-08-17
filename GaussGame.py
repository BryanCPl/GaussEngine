class gaussGame:
    #They are organized to avoid conflicts
    OPN=["<->","*","/","+","-"]
    table=[]
    def __init__(self) -> None:
        self.matrixIdentity=[[1,0,0],[0,1,0],[0,0,1]]

    def setTable(self,table):
        self.table=table

    def showTable(self):
        text=f"{str(self.table[0])} \n {str(self.table[1])} \n {str(self.table[2])}"
        return text
        

    def showMatrixID(self):
        for id in self.matrixIdentity:
                print(id)


    def substracRow(self,m1,m2,r1,r2):
        result=[]
        table2=self.RowOrNum(m2,r2)
        for i in [0,1,2,3]:
            result.append(m1*self.table[r1][i]-table2[i])
        self.table[r1]=result
        
        

    def AddRow(self,m1,m2,r1,r2):
        result=[]

        table2=self.RowOrNum(m2,r2)
        for i in [0,1,2,3]:
            result.append(m1*self.table[r1][i]+table2[i])
        
        self.table[r1]=result


    def MultRows(self,m1,m2,r1,r2):
        result=[]
        table2=self.RowOrNum(m2,r2)
        for i in [0,1,2,3]:
            result.append(m1*self.table[r1][i]+table2[i])
        self.table[r1]=result

    def DivRows(self,m1,m2,r1,r2):
        result=[]
        table2=self.RowOrNum(m2,r2)
        for i in [0,1,2,3]:
            #this is only for dont show negative 0
            if self.table[r1][i]!=0:
                result.append(m1*self.table[r1][i]/table2[i])
            else:
                result.append(m1*self.table[r1][i])
        self.table[r1]=result

    #later for dont repeat code
    def RowManipulation(self,m1,m2,r1,r2,form):
        result=[]
        table2=self.RowOrNum(m2,r2)
        for i in [0,1,2,3]:
            result.append(form)
        self.table[r1]=result

    def RowOrNum(self,m2,r2):
        if r2==None:
            return [m2,m2,m2,m2]
        else:
            result=[]
            for i in self.table[r2]:
                result.append(m2*i)
            return result

    def chageRows(self,r1,r2):
        result=self.table[r1]
        self.table[r1]=self.table[r2]
        self.table[r2]=result

    def defineOperation(self,simbol:str,m1:int,m2:int,r1:int,r2:int):
        
        match simbol:
            case "+":
                self.AddRow(m1,m2,r1,r2)
            case "-":
                self.substracRow(m1,m2,r1,r2)
            case "*":
                self.MultRows(m1,m2,r1,r2)
            case "/":
                self.DivRows(m1,m2,r1,r2)
            case "<->":
                self.chageRows(r1,r2)
            case _:
                return "only accept +,-,*,/"

        self.showTable()

    def operateRows(self,notation:str):
        r1=None
        r2=None
        m1=1
        m2=1
        operation=""
        try:
            operation=self.whichOperation(notation)
            comand=notation.split(operation)

            if len(comand)==2:
                print(comand[0][0],comand[1][0])
                if comand[0][0]!="f":
                    m1=comand[0].split("f")[0]
                if comand[1][0]!="f":
                    m2=comand[1].split("f")[0]

                r1=comand[0].split("f")[1]
                r2=comand[1].split("f")[1]
                r2=int(r2)-1
            else:
                r1=comand[0].split(operation)[0].split("f")[1]
                m2=comand[0].split(operation)[1]

            r1=int(r1)-1
            
            
            
            print(f"{m1}f{r1}{operation}{m2}f{r2}")
            self.defineOperation(operation,int(m1),int(m2),r1,r2) # type: ignore
            return self.showTable()
        except:
            return "El comando no es valido prueba de nuevo"


    def whichOperation(self,n):
        for o in self.OPN:
            if o in n:
                return o
        return "Error,No valid operation"
