" dotvim config {
    let g:dotvim_settings = {}
    let g:dotvim_settings.version = 1

    let g:dotvim_settings.plugin_groups_include = ['python']
    let g:dotvim_settings.max_column = 80

    let g:load_doxygen_syntax=1
    let g:airline_powerline_fonts=1

    " " install YouCompleteMe {
    "     let g:neobundle#install_process_timeout = 9999 
    "     let g:dotvim_settings.autocomplete_method = 'ycm'
    " " }
" }

runtime! ftplugin/man.vim

inoremap jk <ESC>
map <Tab> %


" binding to use vim-over for search and replace word under cursor in file
" uses the b register
nnoremap ;' "bye:OverCommandLine<CR>%s:<C-r>b::g<left><left>
nnoremap ;; :OverCommandLine<CR>%s::g<left><left>

source ~/git/dotvim/vimrc

nnoremap <F10> :Dispatch<CR>

set tabstop=4
set shiftwidth=4

" FSwitch key bindings {
" https://github.com/terryma/dotfiles/blob/master/.vimrc
    
    " Switch to the file and load it into the current window
    nnoremap <silent> <Leader>of :FSHere<cr>
    " Switch to the file and load it into the window on the right
    nmap <silent> <Leader>ol :FSRight<cr>
    " Switch to the file and load it into a new window split on the right
    nmap <silent> <Leader>oL :FSSplitRight<cr>
    " Switch to the file and load it into the window on the left
    nmap <silent> <Leader>oh :FSLeft<cr>
    " Switch to the file and load it into a new window split on the left
    nmap <silent> <Leader>oH :FSSplitLeft<cr>
    " Switch to the file and load it into the window above
    nmap <silent> <Leader>ok :FSAbove<cr>
    " Switch to the file and load it into a new window split above
    nmap <silent> <Leader>oK :FSSplitAbove<cr>
    " Switch to the file and load it into the window below
    nmap <silent> <Leader>oj :FSBelow<cr>
    " Switch to the file and load it into a new window split below
    nmap <silent> <Leader>oJ :FSSplitBelow<cr>
" }

au BufEnter *.C let b:fswitchdst = 'h'
au BufEnter *.h let b:fswitchdst = 'C' 
au FileType man nnoremap <buffer> q :quit<CR>
nnoremap <F8> :VimuxRunCommand("./glfwMain")<CR>
nnoremap ZAQ :qall!<CR>
nnoremap ZWQ :wqall<CR>

