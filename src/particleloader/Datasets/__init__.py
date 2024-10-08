from particleloader.Datasets.topqcd_jets import topqcd_jets
from particleloader.Datasets.qg_jets import qg_jets
from particleloader.Datasets.SPECTER_ee_dijets import ee_dijets
from particleloader.Datasets.SPECTER_qcd_jets import qcd_jets
from particleloader.Datasets.SPECTER_top_jets import top_jets



loader_dict = {"topqcd_jets": topqcd_jets,
               "qg_jets": qg_jets,
                "SPECTER_ee_dijets": ee_dijets,
                "SPECTER_qcd_jets": qcd_jets,
                "SPECTER_top_jets": top_jets,
               }