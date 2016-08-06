class DataStructure(object):
    def __init__(self, data={}, fields={}):
        if not hasattr(self, 'fields'):
            self.fields = {}

        if fields:
            self.fields = fields

        if data:
            self.init(data)

    def cast(self, var_type, v):
        if var_type == 'int':
            return int(v)
        elif var_type == 'float':
            return float(v)

        return v

    def init(self, data):
        for k, v in data.items():
            if self.fields and k in self.fields.keys():
                var_type = self.fields.get(k)
                v = self.cast(var_type, v)

            setattr(self, k, v)


class RateStruct(DataStructure):
    def __init__(self, *args, **kwargs):
        self.fields = {'state_rate': 'float',
                       'county_rate': 'float',
                       'city_rate': 'float',
                       'combined_district_rate': 'float',
                       'combined_rate': 'float'}
        super(RateStruct, self).__init__(*args, **kwargs)


class CategoryStruct(DataStructure):
    pass
