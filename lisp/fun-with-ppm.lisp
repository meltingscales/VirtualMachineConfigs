(load "util.lisp")

; Q: Dafuq is a PPM?
; A: It's a super simple image format.
;
; See http://netpbm.sourceforge.net/doc/ppm.html
;
; For example, a PPM of: BLACK WHITE
;                        WHITE BLACK
;
; Would look like:
;
; +----coolimage.ppm----+
; | P3                  | 
; | 2 2                 |
; | 16                  |
; | 0  0  0   15 15 15  |
; | 15 15 15  0  0  0   |
; +---------------------+


;Magic number for a PPM.
(defvar magic-number "P3")

(defclass Pixel ()
  (
    (red    :initarg :red     :initform 0   :type integer)
    (green  :initarg :green   :initform 0   :type integer)
    (blue   :initarg :blue    :initform 0   :type integer)
    (depth  :initarg :depth   :initform 16  :type integer)
  )
)

(defclass PPM ()
; A class representing a PPM image.
; It has a width, a height, and a 2d array of pixels, among other things.
  (
    (magic-number :initarg magic-number :initform magic-number    :type string)
    (width        :initarg width        :initform 3               :type integer)
    (height       :initarg height       :initform 3               :type integer)
    (depth        :initarg depth        :initform 16              :type integer)
    (pixels       :initarg pixels       :initform 
      ; A 3x3 grid of black pixels.
      (loop for y from 1 to 3 collect (loop for x from 1 to 3 collect (make-instance 'Pixel)))
                                                                  :type list)
  )
)

(format t "Below, we can see a simple Pixel object.") (newline)
(defvar cool-pixel (make-instance 'Pixel :red 1 :green 1 :blue 1))
(describe cool-pixel)
(newline 2)

(format t "We can access a specific property by TODOing below:~%")


(format t "Now, let's try making a default PPM object...")
