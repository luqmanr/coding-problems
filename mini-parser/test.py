

def nest_list(val, list_str) -> list:
    if len(list_str) == 0:
        return [val]
    return [val, list_str]

if __name__ == '__main__':
    str_list = ['123','456','789']
    list_int = []
    for val in str_list[::-1]:
        list_int = nest_list(int(val) , list_int)
        print(list_int)

# expected output:
#
# NestedInteger{
#     _integer: None, 
#     _list: [
#         NestedInteger{
#             _integer: 123, 
#             _list: []
#         }, 
#         NestedInteger{
#             _integer: None, 
#             _list: [
#                 NestedInteger{
#                     _integer: 456, 
#                     _list: []
#                 }, 
#                 NestedInteger{
#                     _integer: None, 
#                     _list: [
#                         NestedInteger{
#                             _integer: 789, 
#                             _list: []
#                         }
#                     ]
#                 }
#             ]
#         }
#     ]
# }

# current output:
NestedInteger{
    _integer: None, 
    _list: [
        NestedInteger{
            _integer: 123, 
            _list: []
        }, 
        NestedInteger{
            _integer: None, 
            _list: [
                NestedInteger{
                    _integer: None, 
                    _list: [
                        NestedInteger{
                            _integer: 456, 
                            _list: []
                        }, 
                        NestedInteger{
                            _integer: None, 
                            _list: [
                                NestedInteger{
                                    _integer: 789, 
                                    _list: []
                                    }]}]}]}]}
