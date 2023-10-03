import listener
# TODO: find out different watch point identifiers and start creating paths to properly handle them.
def main():
    print("PROGRAM ENTRY POINT");
    while True:
        print("running listener file")
        listener.watch_for_changes()



if __name__=="__main__":
    main()