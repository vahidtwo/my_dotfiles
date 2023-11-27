# If you come from bash you might have to change your $PATH.
 export PATH=$HOME/myScript:$PATH:~/.local/bin:$HOME/.config/composer/vendor/bin

# Path to your oh-my-zsh installation.
  export ZSH="/home/vahid/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="amuse"
# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
    git
    gitfast
    python
    pip
    
    virtualenv
    archlinux
    zsh-autosuggestions
)
source $ZSH/oh-my-zsh.sh
toilet -f mono12 --gay -F border Be Happy
#source ~/.venv/bin/activate
# User configuration
#vscode 
alias c='code .'
#alias vim='nvim'
upcode() {
    echo current version: $(code -v | head -n 1);
    echo unzip source;
    mkdir -p /tmp/vscode-files/;
    tar -C /tmp/vscode-files -xf $1;
    echo remove current version
    sudo rm -rf /opt/vscode;
    echo replace new version
    sudo cp -r /tmp/vscode-files/* /opt/vscode;
    echo create link
    sudo ln -sf /opt/vscode/bin/code /usr/bin/code
    echo updated successfully!
    echo current version: $(code -v | head -n 1);
}
# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#alias petabaddb="mysql -u petabad -p']70{toBba9?j' -P 3377 -h 135.181.134.151 petabad"
alias cl="clear"
alias ll="ls -ltrha"
alias ae="deactivate;source ./.venv/bin/activate"
alias de="deactivate"
alias ec="expressvpn connect"
alias ed="expressvpn disconnect"
alias cdd="cd ~/project/py/django/"
alias cdp="cd ~/project/py"
alias cdfc="cd ~/project/py/fastcrawler"
alias cdplasco="cd ~/project/py/django/plasco/Plasco_backend"
alias cdpy="cd ~/project/py"
alias cdb="cd ~/project/py/django/bernet"
#django
alias dgld="python manage.py loaddata"
alias dgma="python manage.py makemigrations"
alias dgmi="python manage.py migrate"
alias dgtest="python manage.py test"
alias dgme="python manage.py makemessages -l fa --no-location "
alias dgco="python manage.py compilemessages -l fa"
#django bernet
alias dgdr="python manage.py dumpdata account.role account.rolepermission --indent 2 > core/fixtures/role.json"
alias dgdp="python manage.py dumpdata account.permission --indent 2 > core/fixtures/permission.json"
alias update_fixture="python manage.py runscript set_all_role_permissions;dgdr;dgdp"
#docker compose
alias pgau="docker compose -f ~/docker-compose/pgadmin.yaml up -d"
alias pgad="docker compose -f ~/docker-compose/pgadmin.yaml down"
alias elu="docker compose -f ~/docker-compose/elastic.yaml up -d"
alias eld="docker compose -f ~/docker-compose/elastic.yaml down"
#git
alias gcod="git checkout develop"
alias gcos="git checkout staging"
alias gmd="git merge develop"
alias ggpulls="git pull origin staging"
alias update_develop="git checkout develop;git pull staging"
# Added by oh-my-vim
#
export PATH=$PATH:/home/vahid/.oh-my-vim/bin

___MY_VMOPTIONS_SHELL_FILE="${HOME}/.jetbrains.vmoptions.sh"; if [ -f "${___MY_VMOPTIONS_SHELL_FILE}" ]; then . "${___MY_VMOPTIONS_SHELL_FILE}"; fi
