day_1 = "um-deliveries-20140519.txt"
day_2 = "um-deliveries-20140520.txt"
day_3 = "um-deliveries-20140521.txt"

def delivery_report(file):
    """Generate report summarizing deliveries for the day"""
    print "Day {}:\n".format(int(file[19:22])-518)

    # Open source file, parse each line into list of elements
    delivery_log = open(file)
    for line in delivery_log:
        line = line.rstrip()
        delivery_info = line.split('|')

    # Assign list elements to variables
    melon_type = delivery_info[0]
    melon_count = delivery_info[1]
    revenue = delivery_info[2]

    print "Delivered {} {}s for total of ${}".format(count, melon, amount)
    the_file.close()

delivery_report(day_1)
delivery_report(day_2)
delivery_report(day_3)


