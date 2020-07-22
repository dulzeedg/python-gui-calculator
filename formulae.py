class Formulae:
    
    # Cell Residence TIme
    # equation one
    
    @classmethod
    def epochTime(cls, horizontalLength,horizontalPath, verticalLength, verticalPath, mobileSpeed ):
        x = (horizontalLength * (horizontalPath + 1)) / (3 * horizontalPath)
        y = (verticalLength * (verticalPath + 1)) / (3 * verticalPath)
        z = (x + y) * 1 / mobileSpeed
        return z

    # equation two
    @classmethod
    def pauseTime(cls, epochTime):
        x = 0.5 * epochTime
        return x

    # equation three
    @classmethod
    def mobilityRate(cls, avgSpeed):
        x = 1 / avgSpeed
        return x

    # equation four
    @classmethod
    def cellCrossing(cls, numberHzRoad, numberVRoad):
        x = 1 / numberHzRoad
        y = 1 / numberVRoad
        z = x + y
        return z

    # equation five
    @classmethod
    def cellResidenceTime(cls, epochTime, pauseTime, mobilityRate, cellCrossing):
        x = epochTime + pauseTime + mobilityRate
        y = x / cellCrossing
        return y


    # Hand Off Delay
    # equation 7
    #equation eight
    @classmethod
    def partialHandoffDelay(cls, probWirelessLinkFailure, linkServingMobileProducer, wiredLinkBandwidth, wirelessLinkBandwidth):
        x = probWirelessLinkFailure / (1 - probWirelessLinkFailure)
        y = linkServingMobileProducer / wirelessLinkBandwidth
        z = x * y + wiredLinkBandwidth
        return z
    @classmethod
    def totalHandoffDelay(cls, linkDelay, partialHandoffDelay):
        x = linkDelay + partialHandoffDelay
        return x
    # equation 9 taking hop distances into consideration
    @classmethod
    def partialHandoffDelay2(cls, partialHandoffDelay, hmrAr, wL,wD, wiredLinkBandwidth, wirelessLinkBandwidth):
        x = ((wL / wiredLinkBandwidth) + wirelessLinkBandwidth)
        y = (hmrAr * (wD / wiredLinkBandwidth) + wirelessLinkBandwidth)
        # float 
        z = partialHandoffDelay * (x + y)
        return z


    # Packet Loss
    # equation thirteen
    @classmethod
    def packetLoss(cls, sessionLength, mobilityRate, numberServingMobileProducers):
        x = sessionLength + mobilityRate + numberServingMobileProducers
        return x

    # total cell residence time
    @classmethod
    def totalCellResidenceTime(cls, radiusOfCell, avgNDNProducerSpeed):
        x = 2 * radiusOfCell
        y = x / avgNDNProducerSpeed
        return y
    
    #equation fourteen
    @classmethod
    def packetLossRatio(cls, packetLoss, totalCellResidenceTime):
        x = packetLoss / totalCellResidenceTime
        y = x * 100
        return y


    # Signal Cost Params
    # equation eighteen
    @classmethod
    def signalCost(cls, cellResidenceTime, numberServingMobileProducers, G, H):
        x = 1 / (cellResidenceTime / 4)
        y = G + H
        z = x * numberServingMobileProducers * y
        return z
    
    # equation nineteen
    @classmethod
    def signalCosting(cls, cellResidenceTime, numberServingMobileProducers, F):
        x = 1 / (cellResidenceTime / 4)
        y = x * numberServingMobileProducers * F
        return y
    
    # cost of signalling content msgs for fast network registration 
    @classmethod
    def G(cls, accessGatewayReg, lengthHandoffInit, wiredLinkBandwidth, wirelessLinkBandwidth, lengthHandoffAck):
        x = wirelessLinkBandwidth * (lengthHandoffInit / wiredLinkBandwidth)
        y = wirelessLinkBandwidth * (lengthHandoffAck / wiredLinkBandwidth)
        z = (accessGatewayReg * x) + (accessGatewayReg * y)
        return z

    # new access gateway registration for serving mobile prodicer
    @classmethod
    def H(cls, probWirelessLinkFailure, acessGatewaySMP, linkServingMobileProducer, wiredLinkBandwidth):
        x = (probWirelessLinkFailure * acessGatewaySMP) / (1 - probWirelessLinkFailure)
        y = (linkServingMobileProducer / wiredLinkBandwidth) + wiredLinkBandwidth
        z = x * y
        return z


    # Packet Delivery Cost
    # equation 21
    @classmethod
    def packetDeliveryCost(cls, numberServingMobileProducers, sessionLength, mobilityRate, weightFactor):
        x = numberServingMobileProducers * sessionLength * mobilityRate * weightFactor
        return x
    
    # equation twentytwo
    @classmethod
    def pDc(cls, Nmr, sessionLength, mobilityRate, totTunnelingCostBenchmarkedPNEMO):
        x = Nmr * sessionLength * mobilityRate *totTunnelingCostBenchmarkedPNEMO
        return x
    
    # equation twentythree 23
    @classmethod
    def pDC(cls, subnetCrossingRate, prodPauseTime, prodSpeed, sizeInterestPacket, sizeDataPAcket, area, HopDistance):
        x = sizeInterestPacket * ((2 * HopDistance) + HopDistance) + sizeDataPAcket + ((2 * HopDistance) + (2 * HopDistance))
        return x
