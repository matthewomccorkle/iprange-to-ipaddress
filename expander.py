import argparse
import ipaddress

def expand_ip_range(ip_range):
    start, end = ip_range.split('-')
    start_ip = ipaddress.ip_address(start.strip())
    end_ip = ipaddress.ip_address(end.strip())

    ip_list = []
    for ip in range(int(start_ip), int(end_ip) + 1):
        ip_list.append(str(ipaddress.ip_address(ip)))

    return ip_list

def process_input(input_file, output_file):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()
                if '-' in line:
                    ip_range_list = expand_ip_range(line)
                    for ip in ip_range_list:
                        outfile.write(ip + '\n')
                else:
                    outfile.write(line + '\n')

def main():
    parser = argparse.ArgumentParser(description="Convert IP address ranges to individual IP addresses")
    parser.add_argument("-i", "--input", help="Input file containing IP address ranges", required=True)
    parser.add_argument("-o", "--output", help="Output file to store individual IP addresses", required=True)
    
    args = parser.parse_args()
    
    process_input(args.input, args.output)

if __name__ == "__main__":
    main()
