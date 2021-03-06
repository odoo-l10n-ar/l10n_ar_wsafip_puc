##################################################
# file: Service_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/bin/wsdl2py -b service.wsdl
# 
##################################################

from Service_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI
from ZSI.generate.pyclass import pyclass_type

# Locator
class ServiceLocator:
    ServiceSoap_address = "http://servicios1.afip.gov.ar/wsfe/service.asmx"
    def getServiceSoapAddress(self):
        return ServiceLocator.ServiceSoap_address
    def getServiceSoap(self, url=None, **kw):
        return ServiceSoapSOAP(url or ServiceLocator.ServiceSoap_address, **kw)

# Methods
class ServiceSoapSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: FERecuperaQTYRequest
    def FERecuperaQTYRequest(self, request, **kw):
        if isinstance(request, FERecuperaQTYRequestSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.facturaelectronica/FERecuperaQTYRequest", **kw)
        # no output wsaction
        response = self.binding.Receive(FERecuperaQTYRequestSoapOut.typecode)
        return response

    # op: FEDummy
    def FEDummy(self, request, **kw):
        if isinstance(request, FEDummySoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.facturaelectronica/FEDummy", **kw)
        # no output wsaction
        response = self.binding.Receive(FEDummySoapOut.typecode)
        return response

    # op: FERecuperaLastCMPRequest
    def FERecuperaLastCMPRequest(self, request, **kw):
        if isinstance(request, FERecuperaLastCMPRequestSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.facturaelectronica/FERecuperaLastCMPRequest", **kw)
        # no output wsaction
        response = self.binding.Receive(FERecuperaLastCMPRequestSoapOut.typecode)
        return response

    # op: FEUltNroRequest
    def FEUltNroRequest(self, request, **kw):
        if isinstance(request, FEUltNroRequestSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.facturaelectronica/FEUltNroRequest", **kw)
        # no output wsaction
        response = self.binding.Receive(FEUltNroRequestSoapOut.typecode)
        return response

    # op: FEAutRequest
    def FEAutRequest(self, request, **kw):
        if isinstance(request, FEAutRequestSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.facturaelectronica/FEAutRequest", **kw)
        # no output wsaction
        response = self.binding.Receive(FEAutRequestSoapOut.typecode)
        return response

    # op: FEConsultaCAERequest
    def FEConsultaCAERequest(self, request, **kw):
        if isinstance(request, FEConsultaCAERequestSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.facturaelectronica/FEConsultaCAERequest", **kw)
        # no output wsaction
        response = self.binding.Receive(FEConsultaCAERequestSoapOut.typecode)
        return response

FERecuperaQTYRequestSoapIn = GED("http://ar.gov.afip.dif.facturaelectronica/", "FERecuperaQTYRequest").pyclass

FERecuperaQTYRequestSoapOut = GED("http://ar.gov.afip.dif.facturaelectronica/", "FERecuperaQTYRequestResponse").pyclass

FEDummySoapIn = GED("http://ar.gov.afip.dif.facturaelectronica/", "FEDummy").pyclass

FEDummySoapOut = GED("http://ar.gov.afip.dif.facturaelectronica/", "FEDummyResponse").pyclass

FERecuperaLastCMPRequestSoapIn = GED("http://ar.gov.afip.dif.facturaelectronica/", "FERecuperaLastCMPRequest").pyclass

FERecuperaLastCMPRequestSoapOut = GED("http://ar.gov.afip.dif.facturaelectronica/", "FERecuperaLastCMPRequestResponse").pyclass

FEUltNroRequestSoapIn = GED("http://ar.gov.afip.dif.facturaelectronica/", "FEUltNroRequest").pyclass

FEUltNroRequestSoapOut = GED("http://ar.gov.afip.dif.facturaelectronica/", "FEUltNroRequestResponse").pyclass

FEAutRequestSoapIn = GED("http://ar.gov.afip.dif.facturaelectronica/", "FEAutRequest").pyclass

FEAutRequestSoapOut = GED("http://ar.gov.afip.dif.facturaelectronica/", "FEAutRequestResponse").pyclass

FEConsultaCAERequestSoapIn = GED("http://ar.gov.afip.dif.facturaelectronica/", "FEConsultaCAERequest").pyclass

FEConsultaCAERequestSoapOut = GED("http://ar.gov.afip.dif.facturaelectronica/", "FEConsultaCAERequestResponse").pyclass
