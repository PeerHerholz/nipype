# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import DWIBiasCorrect


def test_DWIBiasCorrect_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        bias=dict(argstr='-bias %s', ),
        bval_scale=dict(argstr='-bvalue_scaling %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fsl_grad=dict(
            argstr='-fslgrad %s %s',
            xor=('mrtrix_grad', 'fsl_grad'),
        ),
        grad_file=dict(argstr='-grad %s', ),
        grad_fsl=dict(argstr='-fslgrad %s %s', ),
        in_bval=dict(),
        in_bvec=dict(argstr='-fslgrad %s %s', ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        in_mask=dict(argstr='-mask %s', ),
        mrtrix_grad=dict(
            argstr='-grad %s',
            xor=('mrtrix_grad', 'fsl_grad'),
        ),
        nthreads=dict(
            argstr='-nthreads %d',
            nohash=True,
        ),
        out_file=dict(
            argstr='%s',
            genfile=True,
            keep_extension=True,
            name_source='in_file',
            name_template='%s_biascorr',
            position=-1,
        ),
        use_ants=dict(
            argstr='-ants',
            usedefault=True,
            xor=('use_ants', 'use_fsl'),
        ),
        use_fsl=dict(
            argstr='-fsl',
            min_ver='5.0.10',
            xor=('use_ants', 'use_fsl'),
        ),
    )
    inputs = DWIBiasCorrect.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DWIBiasCorrect_outputs():
    output_map = dict(
        bias=dict(),
        out_file=dict(),
    )
    outputs = DWIBiasCorrect.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
