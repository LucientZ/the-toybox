nocompatible
syntax on
set smartindent
set tabstop=4
set shiftwidth=4
set noexpandtab

set viminfo='10,\"100,:20,%,n~/.viminfo

" turns off autoindent when pasting
nnoremap \tp :set invpaste paste?<CR>
nmap <F4> \tp
imap <F4> <C-O>\tp
set pastetoggle=<F4>

" display the current mode and partially-typed commands in the status line:
set showmode
set showcmd
set ruler       " show the cursor position all the time
set foldenable
set foldmethod=marker

function! ResCur()
    if line("'\"") <= line("$")
        normal! g`"
        return 1
    endif
endfunction

augroup resCur
    autocmd!
    autocmd BufWinEnter * call ResCur()
augroup END

autocmd FileType python set tabstop=4|set shiftwidth=4|set expandtab
autocmd FileType json set tabstop=4|set shiftwidth=4|set expandtab
autocmd FileType sh set tabstop=4|set shiftwidth=4|set noexpandtab
autocmd FileType c set tabstop=4|set shiftwidth=4|set noexpandtab
autocmd FileType ruby set tabstop=2|set shiftwidth=2|set expandtab
autocmd BufWritePre * :%s/\s\+$//e

filetype on
filetype indent on
filetype plugin on
iab validataion validation

" Robbie's stuff
set number
set cursorlineopt=number
hi LineNr ctermfg=218
hi CursorLineNr ctermfg=grey
if has('nvim')
    colorscheme hatsunemiku
    set viminfo+=n~/.config/nvim/viminfo
endif