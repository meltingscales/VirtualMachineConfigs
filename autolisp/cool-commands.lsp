(defun assert-equal (actual expected)
"Assert that two objects are the same.
Uses 'equal'."
 
  (if (not (equal actual expected)) 
    (progn 
      (princ (strcat (vl-princ-to-string actual ) " does not equal " (vl-princ-to-string expected) ))
      (princ (strcat "Got " (vl-princ-to-string actual) " instead!"))
      nil ;Return nil as we've failed
    )
  )
t ; Return t as we've passed
)

(defun slope (p1 p2)
"Given two points, return a vector that points at p2 from p1's perspective.

Examples:

(slope '(4 4 4) '(7 7 7)) = '(1 1 1)
(slope '(0 0 0) '(1 2 0)) = '(1 2 0)
"
)

(defun offset (p1 p2)
"Given two points, return a new point that represents the offset from P1 to the other.

Examples:

(offset '(1 1 1) '(2 2.5 2)) = '(-1 -1.5 -1)
(offset '(2 2.5 2) '(1 1 1)) = '(1 1.5 1)

"

  (setq i 0)
  (setq p3 '())
  
  (while (< i (length p1))

    (setq p3
      (append p3 (list (- (nth i p1) (nth i p2) )) )
    ) ; Append to P3 the difference between one dimension of P1 and P2.

    (setq i (+ i 1)) ; Next dimension.
  )

  p3 ; Return P3.
)

; Test our offset function.
(assert-equal (offset '(0 0 0) '(0 0 0))    '(0 0 0))
(assert-equal (offset '(0 0 0) '(1 1 1))    '(-1 -1 -1))
(assert-equal (offset '(1 1 1) '(0 0 0))    '(1 1 1))
(assert-equal (offset '(1 1 1) '(2 2.5 2))  '(-1 -1.5 -1))

(defun move-point (p1 p2 dist)
"Returns a new point, p3, which is p1 moved towards p2 by 'dist'.
Can move p1 beyond p2.

Example:

(move-point '(0 0 0) '(1 1 0) 1) = '(0.4142 0.4142 0)       ; This is moving one unit to the NE, hence the (sqrt(2) - 1)
(move-point '(0 0 0) '(0.7071 0.7071 0) 1) = '(0.5 0.5 0)   ; This is moving (sqrt(0.5)) units to the NE, which moves you to (0.5,0.5)

"
  nil ;TODO math things
)

(defun add-em (x y)
"Given an 'x' and a 'y', add them together."
  (+ x y)
)

; TODO actually make circles instead of printing 'po ta to'
(defun c:circle_line (/ startp endp number)
"Makes a line of circles."

  (setq number (getint "How many circles:"))
  (setq startp (getpoint "Start point:"))
  (setq endp   (getpoint "End point:"))
  
  (setq i 0) ; Start at 0
  
  (while (< i number) ; From 0 to number,
    (princ "po ta to") ; TODO actually create circle...
    (setq i (+ i 1)) ; Increment i
  )

  i ; Return i because why not.
)

(defun c:redcircle (/ center pt-on-circumference)
"Custom command that lets you make a red circle."
  (terpri)
  (setq center (getpoint "Center of red circle")) ; Get center from user
  (terpri)
  (setq pt-on-circumference (getpoint center "Pick a point on the circumference:")) ; Get point on circumference
  (command "_circle" center pt-on-circumference) ; Make the circle.
  (command "_chprop" "_last" "" "_color" "red" "") ; Make it red.
)
