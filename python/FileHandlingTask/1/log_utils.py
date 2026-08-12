
def parse_line(line):
        parts = line.split(maxsplit=3)
        level = parts[2]                         #  def parse_line(line):
        message = parts[3]                      # message= " ".join(parts[3:])
        return level,message                     #  return (level,message)

                                                    #def read_logs(path):
                                                     # entries=[]
def read_logs(path):                                  # with open(path,"r") as file
        logs = []                                      # line = line.strip()
        with open(path,"r") as file:                      #if line:
                for line in file:                             #entries.append(pare+line())
                        level,message = parse_line(line)   #return entires
                        logs.append((level,message))
        return logs
        

