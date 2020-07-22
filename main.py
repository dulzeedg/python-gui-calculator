

from formulae import Formulae

# collect all inputs
# check for dependence of parameters on > 1 global inputs
# Global Variables
# launch notebook




class ParamsCalculate:
    
    results = []
    valuesName = []

    def cellResidenceTime(self, results = results, valuesName = valuesName ):
        # self.results = results
        # self.valuesName = valuesName
        # perform calc then store in list
        # Accepts user input
        print("Calculating the value of Cell Residence Time")
        hL = float(input("Enter Horizontal Length:\n"))
        hP = float(input("Enter Horizontal Path   "))
        vL = round(float(input("Enter Vertical Length   ")), 2)
        vP = round(float(input("Enter Horizontal Path   ")), 2)
        mS = round(float(input("Enter Mobile Producer Speed ")), 2)
        mR = round(float(input("Enter Mobility Rate ")),2)
        HzR = round(float(input("Number of Horizontal Road  ")), 2)
        VtR = round(float(input("Number of Vertical Road    ")), 2)
        # append to lists results
        results.append(round(Formulae.epochTime(hL,hP,vL,vP,mS), 2))
        # print(results[0])
        valuesName.append("epochTime")
        # print(results[0])
        results.append(round(Formulae.pauseTime(results[0]),2)) #1
        valuesName.append("pauseTime")
        # print(results[1])
        results.append(round(Formulae.cellCrossing(HzR,VtR), 2)) #2
        valuesName.append("cellCrossing")
        #3
        results.append(round(Formulae.cellResidenceTime(results[0],results[1],mR,results[2]), 2))
        valuesName.append("cellResidenceTime")
        y = valuesName[3]
        z = results[3]
        return y, z

    

    def handoffDelay(self, results = results, valuesName = valuesName):
        print("Hand Off Delay")
        pWlf = float(input("Probability of wireless link failure  "))
        lSMP = float(input("Link of serving mobile producers  "))
        Wwd = float(input("Bandwidth of wired link    "))
        Wwl = float(input("Bandwidth of wireless Link    "))
        lD = float(input("Link Delay  "))
        hopDmrar = float(input("Horizontal distance btw mobile Router and Acess Router    "))
        wl = float(input("Wireless Link   "))
        wD = float(input("Wired Link  "))
        results.append(round(Formulae.partialHandoffDelay(pWlf,lSMP,Wwd,Wwl),2)) #4
        valuesName.append("partialhandOffDelay")
        results.append(round(Formulae.totalHandoffDelay(lD,results[4]), 2)) #5
        valuesName.append("totalHandOffDelay")
        #6
        results.append(round(Formulae.partialHandoffDelay2(results[4],hopDmrar,wl,wD,Wwd,Wwl),2))
        valuesName.append("partialHandOffDelay2")
        i = valuesName[4]
        j = valuesName[4]
        a = valuesName[5]
        b = results[5]
        y = valuesName[6]
        z = results[6]
        return i , j, a, b, y, z
    
    def signalCost(self, results = results, valuesName = valuesName):
        print("Signal Cost")
        nSMP = float(input("Number of Serving Mobile Producers "))
        aGr = float(input("Acces gateway registration  "))
        lHDi = float(input("Length of handoff initialization"))
        lAck = float(input("Length of Acknowledgement"))
        aGsmP = float(input("Access gateway Serving mobile producers"))
        results.append(round(Formulae.G(aGr,lHDi,Wwd,Wwl,lAck),2)) #7
        valuesName.append("Cost of Signal msgs for fast Net Reg")
        results.append(round(Formulae.H(pWlf,aGsmP,lSMP,Wwd),2)) #8
        valuesName.append("New access gateway Reg for SMP")
        results.append(round(Formulae.signalCost(results[3], nSMP, results[7], results[8]),2)) #9
        valuesName.append("Signal Cost")
        y = valuesName[9]
        z = results[9]
        return y, z

    def packetLoss(self, results = results, valuesName = valuesName):
        print("Packet Loss")
        sL = float(input("Session Length  "))
        rC = float(input("Radius of Cell  "))
        pS = float(input("Average NDN producer speed  "))
        results.append(round(Formulae.packetLoss(sL,mR,nSMP),2)) #10
        valuesName.append("packetLoss")
        results.append(round(float(Formulae.totalCellResidenceTime(rC,pS)),2)) # 11
        valuesName.append("totalCellResidenceTime")
        results.append(round(float(Formulae.packetLossRatio(results[10],results[11])),2)) #12
        valuesName.append("packetlossRatio")
        y = valuesName[12]
        z = results[12]
        return y, z







## join both list then print new list
# print(results)
# print(valuesName)