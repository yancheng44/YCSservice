# -*- coding:utf-8 -*-

import xml.dom.minidom as Dom


"""
<RequestXml>
    <TxnRefNo>20171218101915</TxnRefNo>
    <ClientId>000000088464</ClientId>
    <BranchId>QWG540AZ</BranchId>
    <ProductCode>LVNPRD</ProductCode>
    <OrderNumber>YCS0066984</OrderNumber>
    <TotalAmount>500</TotalAmount>
    <OrderDetails>
        <FaceValue>500</FaceValue>
        <Quantity>1</Quantity>
        <Currency>CNY</Currency>
        <TotalAmount>500</TotalAmount>
        <CardType>No</CardType>
    </OrderDetails>
</RequestXml>

"""

from datetime import datetime

def _get_uid():
    #基于时间的流水号
    return datetime.now().strftime('%Y%m%d%H%M%S')


class XMLGenerator:
    def __init__(self, xml_name):
        self.doc = Dom.Document()
        self.xml_name = xml_name

    def createNode(self, node_name):
        return self.doc.createElement(node_name)

    def addNode(self, node, prev_node=None):
        cur_node = node
        if prev_node is not None:
            prev_node.appendChild(cur_node)
        else:
            self.doc.appendChild(cur_node)
        return cur_node

    def setNodeAttr(self, node, att_name, value):
        cur_node = node
        cur_node.setAttribute(att_name, value)

    def setNodeValue(self, cur_node, value):
        node_data = self.doc.createTextNode(value)
        cur_node.appendChild(node_data)

    #如果需要可以保存xml文档
    def saveXml(self):
        f = open(self.xml_name, "w")
        f.write(self.doc.toprettyxml(indent="\t", newl="\n", encoding="utf-8"))
        f.close()

    def getXml(self):
        return self.doc.toprettyxml()



def create_order_xml():
    orderXML = XMLGenerator("TXN")

    #root
    request = orderXML.createNode("RequestXml")
    orderXML.addNode(node=request)

    #TxnRefNo
    txn = orderXML.createNode("TxnRefNo")
    orderXML.setNodeValue(txn, _get_uid())
    orderXML.addNode(txn, request)

    #ClientId
    clientid = orderXML.createNode("ClientId")
    orderXML.setNodeValue(clientid, "000000088464")
    orderXML.addNode(clientid, request)

    #branchid
    branchid = orderXML.createNode("BranchId")
    orderXML.setNodeValue(branchid, "QWG540AZ")
    orderXML.addNode(branchid, request)

    #ProductCode
    productcode = orderXML.createNode("ProductCode")
    orderXML.setNodeValue(productcode, "LVNPRD")
    orderXML.addNode(productcode, request)


    #OrderNumber
    ordernumber = orderXML.createNode("OrderNumber")
    orderXML.setNodeValue(ordernumber, "YCS0066984")
    orderXML.addNode(ordernumber, request)

    #TotalAmount

    totalamount = orderXML.createNode("TotalAmount")
    orderXML.setNodeValue(totalamount, "500")
    orderXML.addNode(totalamount, request)


    #处理多条detail

    """
    <OrderDetails>
        <FaceValue>500</FaceValue>
        <Quantity>1</Quantity>
        <Currency>CNY</Currency>
        <TotalAmount>500</TotalAmount>
        <CardType>No</CardType>
    </OrderDetails>
    """
    lines = [("200", "2", "400", "NO"), ("100", "3", "300", "NO")]

    for z in range(len(lines)):

        detail = orderXML.createNode("OrderDetails")

        facevalue = orderXML.createNode("FaceValue")
        orderXML.setNodeValue(facevalue, lines[z][0])
        orderXML.addNode(facevalue, detail)

        quantity= orderXML.createNode("Quantity")
        orderXML.setNodeValue(quantity, lines[z][1])
        orderXML.addNode(quantity, detail)

        currenct = orderXML.createNode("Currency")
        orderXML.setNodeValue(currenct, "CNY")
        orderXML.addNode(currenct, detail)

        totalamount = orderXML.createNode("TotalAmount")
        orderXML.setNodeValue(totalamount, lines[z][2])
        orderXML.addNode(totalamount, detail)

        cardtype = orderXML.createNode("CardType")
        orderXML.setNodeValue(cardtype, lines[z][3])
        orderXML.addNode(cardtype, detail)

        orderXML.addNode(detail, request)

    return orderXML.getXml()


if __name__ == "__main__":
    order = create_order_xml()
    print(order)






