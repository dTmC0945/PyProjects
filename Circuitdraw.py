import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += (Q := elm.IcDIP(pins=8)
                 .label('Offset Null', loc='p1', fontsize=10)
                 .label('Inverting Input', loc='p2', fontsize=10)
                 .label('Non-inverting Input', loc='p3', fontsize=10)
                 .label('V-', loc='p4', fontsize=10)
                 .label('Offset Null', loc='p5', fontsize=10)
                 .label('Output', loc='p6', fontsize=10)
                 .label('V+', loc='p7', fontsize=10)
                 .label('NC', loc='p8', fontsize=10))
    d += elm.Line().at(Q.p2_in).length(d.unit/5)
    d += (op := elm.Opamp().anchor('in1').scale(.8))
    d += elm.Line().at(Q.p3_in).length(d.unit/5)
    d += elm.Wire('c', k=.3).at(op.out).to(Q.p6_in)
    d += elm.Wire('-|').at(Q.p4_in).to(op.n1)
    d += elm.Wire('-|').at(Q.p7_in).to(op.n2)