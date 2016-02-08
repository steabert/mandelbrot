      SUBROUTINE MANDELBROT (XOFF, YOFF, XRANGE, YRANGE,
     &                       RES, MXSTEP, BROT)
* In python, this function is called as
* mandelbrot (xOff, yOff, xRange, yRange, Res, mxStep, fMatrix)
      IMPLICIT NONE
      INTEGER I, J, IMAX, JMAX
      INTEGER, INTENT(IN) :: RES
      INTEGER ITER
      INTEGER, INTENT(IN) :: MXSTEP
      INTEGER, INTENT(INOUT) :: BROT(*)
      REAL*8, INTENT(IN) :: XRANGE, YRANGE, XOFF, YOFF
      REAL*8 X0, Y0, XOLD, YOLD, XNEW, YNEW
      IMAX=INT(RES * XRANGE)
      JMAX=INT(RES * YRANGE)
      DO I=1,IMAX
       DO J=1,JMAX
        ITER=0
        X0=DBLE(I)/DBLE(RES)+XOFF
        Y0=DBLE(J)/DBLE(RES)+YOFF
        XOLD=X0
        YOLD=Y0
        DO WHILE(.NOT.
     &   ((XOLD*XOLD+YOLD*YOLD.GT.4.0).OR.(ITER.GT.MXSTEP)))
         XNEW=XOLD*XOLD-YOLD*YOLD+X0
         YNEW=2*XOLD*YOLD+Y0
         XOLD=XNEW*XNEW-YNEW*YNEW+X0
         YOLD=2*XNEW*YNEW+Y0
         ITER=ITER+2_1
        ENDDO
        BROT(J+JMAX*(I-1))=ITER
       ENDDO
      ENDDO
      END SUBROUTINE
