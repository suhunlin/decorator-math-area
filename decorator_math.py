class Math:
    def __init__(self):
        print(self, 'object was create!!!')

    def do_other_thing(func):
        def other_thing(self, type, *args, **kwargs):
            print('This calculate is for', type, 'area!!!area is:')
            return func(self, type, *args, **kwargs)
        return other_thing

    @do_other_thing
    def cal_area(self, type, *args, **kwargs):
        area = 0
        if not args:
            print('No data to calculate area!!!')
        else:
            if type == 'round':
                area = args[0] * args[0] * 3.14
            elif type == 'rectangular':
                try:
                    area = args[0] * args[1]
                except Exception as error_message:
                    print(error_message)
        return area

def main():
    m1 = Math()
    print(m1.cal_area('rectangular', 3, 4))

if __name__ == '__main__':
    main()