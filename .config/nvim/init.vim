set number
syntax on
set vb

set mouse=a
set undofile

set shiftwidth=4
set tabstop=4
set expandtab
set showcmd
set showmatch
set incsearch
set tw=80
set autoindent

call plug#begin('~/.vim/plugged')
Plug 'junegunn/goyo.vim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'ctrlpvim/ctrlp.vim'
" Plug 'Yggdroot/indentLine'

Plug 'morhetz/gruvbox'
call plug#end()

colorscheme gruvbox
set t_Co=256
set background=dark

map <C-f> :Goyo<CR>

noremap tt :tab split<CR>
cmap w!! w !sudo tee > /dev/null %

if maparg('<C-L>', 'n') ==# ''
    nnoremap <silent> <C-L> :nohlsearch<CR><C-L>
endif

" air-line

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

" unicode symbols
let g:airline_left_sep = ' '
let g:airline_left_sep = ' '
let g:airline_right_sep = ' '
let g:airline_right_sep = ' '
let g:airline_symbols.linenr = ' '
let g:airline_symbols.linenr = ' '
let g:airline_symbols.linenr = ' '
let g:airline_symbols.branch = ' '
let g:airline_symbols.paste = ' '
let g:airline_symbols.paste = ' '
let g:airline_symbols.paste = ' '
let g:airline_symbols.whitespace = ' '

" airline symbols
let g:airline_left_sep = ' '
let g:airline_left_alt_sep = ' '
let g:airline_right_sep = ' '
let g:airline_right_alt_sep = ' '
let g:airline_symbols.branch = ' '
let g:airline_symbols.readonly = ' '
let g:airline_symbols.linenr = ' '
