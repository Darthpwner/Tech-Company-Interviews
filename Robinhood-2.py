# Enter your code here. Read input from STDIN. Print output to STDOUT

scheduler_queue = []

def bad_transfer(src_account, dst_account, amount):
    # Lock src_cash and src_account.cash resources until we are certain that they are up to date
    priority_queue.append(current_transaction)
    
    while not locked:
        acquire lock
        alert other threads that resource not available
        
        src_cash = src_account.cash # DB read
        dst_cash = dst_account.cash # DB read
    
        if src_cash < amount:
            raise InsufficientFunds
    
        src_account.cash = src_cash - amount # DB write
        src_account.send_src_transfer_email()
        
        dst_account.cash = dst_cash + amount # DB write
        dst_account.send_dst_transfer_email()
        
        release lock
    
