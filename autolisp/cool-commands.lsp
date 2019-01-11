(defun add-em (x y)
"Given an 'x' and a 'y', add them together."
  (+ x y)
)


; TODO actually make circles instead of printing 'po ta to'
(defun make-some-circles ()
"Makes a pretty circle pattern."

  (setq i 0) ; Start at 0
  (setq radius 3) ; Radius is 3
  
  (while (< i 10) ; From 0 to 10,
    (princ "po ta to") ; PO TA TO
    (setq i (+ i 1)) ; Increment i
  )

  i ; Return i because why not.
)

(defun c:redcircle (/ center pt-on-circumference)
"Custom command that lets you make a red circle."
  (terpri)
  (setq center (getpoint "Center of red circle")) ; Get center from user
  (princ (strcat "Center is " (vl-princ-to-string center) ".")) ;debug
  (terpri)
  (setq pt-on-circumference (getpoint center "Pick a point on the circumference:")) ; Get point on circumference
  (command "_circle" center pt-on-circumference) ; Make the circle.
  (command "_chprop" "_last" "" "_color" "red" "") ; Make it red.
)
