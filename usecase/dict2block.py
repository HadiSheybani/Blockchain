from entity.block import Block


class Dict2Block:
    
    def convert(self, block_dict : dict):
        if "index" not in block_dict:
            raise ValueError('No Index Value')
        if 'time_stamp' not in block_dict:
            raise ValueError('No Time Stamp Value')
        if 'data' not in block_dict:
            raise ValueError('No Data Value')
        if 'pre_hash' not in block_dict:
            raise ValueError('No PreHash Value')
        if 'block_hash' not in block_dict:
            raise ValueError('No BlockHash Value')
        return Block(int(block_dict['index']), 
                    int(block_dict['time_stamp']), 
                    block_dict['data'], 
                    block_dict['pre_hash'], 
                    block_dict['block_hash'])