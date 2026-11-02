for %i in fs0 fs1 fs2
  if exist %i:\EFI\Boot\bootx64.efi then
    %i:\EFI\Boot\bootx64.efi
  endif
endfor
