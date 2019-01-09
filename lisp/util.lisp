(defun newline (&optional times) 
"Print a new line 1 or more times."
  
  (progn
    (format t "~%") ; New line.
    
    (cond ; Switch-case.

      ((null times) ; If times is nil, return.
        ())
      
      ((> times 1) ; If times > 1, print another line.
        (newline (- times 1)))
    )
  )
)
