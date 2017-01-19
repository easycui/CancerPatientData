def condition():
    return ['min_PSA','max_PSA','min_prostate_vol','max_prostate_vol','min_lesion_size','max_lesion_size',
                'min_sector','max_sector','min_PIRADS_score','max_PIRADS_score','min_GLEASON_score','max_GLEASON_score']

def attrs():
    return ['patient_ID','PSA','prostate_vol',
            'lesion_size','sector','PIRADS_score','GLEASON_score']