from datetime import datetime
open('today.txt', 'wt').write(str(datetime.utcnow()))
