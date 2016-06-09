from objects_common.jsonObject import JsonObject
from costCharacteristic import CostCharacteristic
from objects_common.arrayType import ArrayType

class TransferCostPac(JsonObject):

    def __init__(self, json_struct=None):
        self.costCharacteristic=ArrayType.factory(CostCharacteristic)
        super(TransferCostPac, self).__init__(json_struct)
