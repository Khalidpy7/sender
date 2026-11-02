#!/bin/bash

# TOOL : SENDER
# VERSION : 1.0
# AUTHOR : KHALID SAIF
# USE THIS TOOL FOR EDUCATIONAL METHODS.

# COLOR CODES
BLACK="$(printf '\033[1;30m')"
RED="$(printf '\033[1;31m')"
GREEN="$(printf '\033[1;32m')"
YELLOW="$(printf '\033[1;33m')"
BLUE="$(printf '\033[1;34m')"
MAGENTA="$(printf '\033[1;35m')"
CYAN="$(printf '\033[1;36m')"
WHITE="$(printf '\033[1;37m')"
RESET="$(printf '\033[0m')"

# CHECKING FOR DEPENDENCIES.
bash -c "clear"
echo -e "${YELLOW}[${MAGENTA}?${YELLOW}]${BLUE} CHECKING DEPENDENCIES. ${RESET}"
sleep 1

CHECK_PACKAGES() {
					
					if dpkg -s "$1" &>/dev/null; then
										echo -e "${BLUE}[${WHITE}*${BLUE}]${GREEN} $1 NOT INSTALLED. ${RESET}"
					else
										echo -e "${YELLOW}[${MAGENTA}?${YELLOW}]${RED} $1 NOT INSTALLED. ${RESET}"
										bash -c "pkg install $1"
										echo 
					fi
					echo
}

CHECK_PACKAGES python
CHECK_PACKAGES python-pip

# INSTALLING "REQUIRMENTS" MODULE.
bash -c "pip install -r requirements.txt"

# RUN PYTHON FILE.
bash -c "python sender.py"





