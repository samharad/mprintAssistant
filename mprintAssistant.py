from printSession import PrintSession
from document import Document
import utils

def main(): 
  # Create new session
  session = PrintSession()

  # Set sysArgs to arguments
  session.setSysArgs(vars(utils.parse()))
  session.interpretSysArgs()

  # Authenticate session
  session.authenticate()

  # Determine printer
  session.determineDestination()

  # Determine documents
  session.determineDocs();




if __name__ == "__main__":
  main()