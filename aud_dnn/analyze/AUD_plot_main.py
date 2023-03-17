import matplotlib.pyplot as plt

from plot_utils_AUD import *
np.random.seed(0)
random.seed(0)

run_diag = False
run_agg = True
plot_subjectwise = False # for checking how plots look per subject
run_surf = False
merge_surface_targets = False
do_stats = False

concat_over_models = False

### Directories ###
date = datetime.datetime.now().strftime("%m%d%Y")
DATADIR = (Path(os.getcwd()) / '..' / '..' / 'data').resolve()
RESULTDIR_LOCAL = (Path(os.getcwd()) / '..' / '..' / 'results').resolve()
PLOTSURFDIR = Path(f'{ROOT}/results/AUD/20210915_median_across_splits_correction/PLOTS_SURF_across-models/')
SURFDIR = f'{DATADIR}/fsavg_surf/'

# Logging
date = datetime.datetime.now().strftime("%m%d%Y-%T")
if user != 'gt':
	sys.stdout = open(join(RESULTDIR_ROOT, 'logs', f'out-{date}.log'), 'a+')

source_models = [  'Kell2018word', 'Kell2018speaker',  'Kell2018music', 'Kell2018audioset', 'Kell2018multitask',
				 'ResNet50word', 'ResNet50speaker', 'ResNet50music', 'ResNet50audioset',   'ResNet50multitask',
				'AST',  'wav2vec', 'DCASE2020', 'DS2', 'VGGish',  'ZeroSpeech2020', 'S2T', 'metricGAN', 'sepformer',
				 'spectemp']
# source_models = [  'Kell2018word', 'Kell2018speaker',  'Kell2018music', 'Kell2018audioset', 'Kell2018multitask',
# 				 'ResNet50word', 'ResNet50speaker', 'ResNet50music', 'ResNet50audioset',   'ResNet50multitask',
# 				'AST',  'wav2vec', 'VGGish', 'S2T',  'sepformer']
# source_models = ['wav2vecpower']
source_models = ['Kell2018word', 'Kell2018speaker',  'Kell2018music', 'Kell2018audioset', 'Kell2018multitask',
				'ResNet50word', 'ResNet50speaker', 'ResNet50music', 'ResNet50audioset',   'ResNet50multitask',]
# source_models = ['AST',  'wav2vec', 'DCASE2020', 'DS2', 'VGGish', 'ZeroSpeech2020', 'S2T', 'metricGAN', 'sepformer']

target = 'B2021'
randnetw = 'False'

print(f'---------- Target: {target} ----------')

if concat_over_models:  # assemble plots across models
	if target != 'NH2015-B2021':
		df_meta_roi = pd.read_pickle(join(DATADIR, 'neural', target, 'df_roi_meta.pkl'))
	
	if target == 'NH2015comp': # components
		
		### For plotting in-house models barplot (Figure 6) ###
		# save_str = f'_task-grouped-ymin-0.2-empty-bar-new-spacing-inhouse-models'
		# # #### Best layer component predictions across models (independently selected layer) ####
		# for sort_flag in [['Kell2018word', 'ResNet50word', 'Kell2018speaker', 'ResNet50speaker', 'Kell2018music',  'ResNet50music',
		# 				   'Kell2018audioset','ResNet50audioset', 'Kell2018multitask','ResNet50multitask',]]: #'performance', NH2015_all_models_performance_order
		# 	for randnetw_flag in ['False', 'True']:
		# 		barplot_components_across_models(source_models=source_models, target=target, df_meta_roi=df_meta_roi,
		# 										 randnetw=randnetw_flag, value_of_interest='median_r2_test',
		# 										 sem_of_interest='median_r2_test_sem_over_it',
		# 										 save=SAVEDIR_CENTRALIZED, save_str=save_str, include_spectemp=True,
		# 										 sort_by=sort_flag, add_in_spacing_bar=True)
				
		### For plotting all models barplot (part of Figure 6) ###
		# save_str = f'_replot-alpha-1'
		# # #### Best layer component predictions across models (independently selected layer) ####
		# for sort_flag in [NH2015_all_models_performance_order]: #'performance', NH2015_all_models_performance_order
		# 	for randnetw_flag in ['True', 'False']: # 'False', 'True'
		# 		barplot_components_across_models(source_models=source_models, target=target, df_meta_roi=df_meta_roi,
		# 										 randnetw=randnetw_flag, value_of_interest='median_r2_test',
		# 										 sem_of_interest='median_r2_test_sem_over_it',
		# 										 save=SAVEDIR_CENTRALIZED, save_str=save_str, include_spectemp=True,
		# 										 sort_by=sort_flag, add_in_spacing_bar=False)

		#### Analyze best layer (not independently selected, just the argmax layer) ####
		# for randnetw_flag in [ 'True']:
		# 	scatter_comp_best_layer_across_models(source_models=source_models, target=target,
		# 									 randnetw=randnetw_flag, aggregation='argmax',
		# 									 save=SAVEDIR_CENTRALIZED, save_str='_inhouse-models_symbols', ylim=[-0.02,1.02],
		# 									 value_of_interest='rel_pos',
		# 									 )
		
		#### Scatter: comp1 vs comp2 predictivity across models ####
		# for randnetw_flag in [ 'False', 'True',]:
		# 	if randnetw_flag == 'False':
		# 		ylim = [0.5, 1]
		# 	else:
		# 		ylim = [0, 1]
		#
		# 	scatter_components_across_models(source_models=source_models, target=target, df_meta_roi=df_meta_roi,
		# 									 randnetw=randnetw_flag, aggregation='CV-splits-nit-10',
		# 									 save=SAVEDIR_CENTRALIZED, save_str='_inhouse-models_symbols-no-err', include_spectemp=False,ylim=ylim,
		# 									 value_of_interest='median_r2_test', sem_of_interest='median_r2_test_sem_over_it')
		#
		# 	# ## Associated statistics - comp1 vs comp2 comparions for models of interest ##
		# 	compare_CV_splits_nit(source_models=source_models, target=target, df_meta_roi=df_meta_roi,
		# 						  save=True, save_str='all-models-bootstrap',
		# 						  models1 = ['Kell2018word', 'Kell2018speaker',  'Kell2018music', 'Kell2018audioset', 'Kell2018multitask',
		# 		 			'ResNet50word', 'ResNet50speaker', 'ResNet50music', 'ResNet50audioset',   'ResNet50multitask',
		# 					'AST',  'wav2vec', 'DCASE2020', 'DS2', 'VGGish',  'ZeroSpeech2020', 'S2T', 'metricGAN', 'sepformer'],
		# 						  models2 = ['Kell2018word', 'Kell2018speaker',  'Kell2018music', 'Kell2018audioset', 'Kell2018multitask',
		# 		 			'ResNet50word', 'ResNet50speaker', 'ResNet50music', 'ResNet50audioset',   'ResNet50multitask',
		# 					'AST',  'wav2vec', 'DCASE2020', 'DS2', 'VGGish',  'ZeroSpeech2020', 'S2T', 'metricGAN', 'sepformer'],
		# 						  aggregation='CV-splits-nit-10',
		# 						  randnetw=randnetw_flag,)
			# compare_CV_splits_nit(source_models=source_models, target=target, save=True, save_str='inhouse-models_CochResNet50-bootstrap',
			# 					  models1=['ResNet50word', 'ResNet50speaker', 'ResNet50multitask','ResNet50audioset', 'ResNet50music'],
			# 					  models2=['ResNet50word', 'ResNet50speaker', 'ResNet50multitask','ResNet50audioset', 'ResNet50music'],
			# 					  aggregation='CV-splits-nit-10',
			# 					  randnetw=randnetw_flag, )
		
		
		#### Predicted versus actual components (independently selected layer - most frequent one) ####
		savestr = '_with_p-vals-TEST'
		for source_model in source_models:
			for randnetw_flag in ['False','True']:
				if source_model == 'spectemp' and randnetw_flag == 'True':
					continue
				scatter_NH2015comp_resp_vs_pred(source_model=source_model, target=target, df_meta_roi=df_meta_roi,
												randnetw=randnetw_flag, save=SAVEDIR_CENTRALIZED, add_savestr=savestr)
	
	elif target == 'NH2015-B2021':
		# DETERMINE COLOR SCALE FOR SURFACE MAPS (also copied over to target = NH2015-B2021, but leaving here for now)
		# if len(source_models) == 19: # All
		# 	for randnetw_flag in ['False', 'True']:
		# 		determine_surf_layer_colorscale(target='NH2015-B2021', source_models=source_models, randnetw=randnetw_flag,
		# 										save=PLOTSURFDIR)
		print('Done!')

	
	elif target == 'NH2015' or target == 'B2021': # neural data, either Nh2015 or B2021
		# BARPLOTS ACROSS MODELS
		# for sort_flag in [B2021_all_models_performance_order]:
		# 	for val_flag in ['median_r2_test_c', ]: # 'median_r2_test_c', 'median_r2_test'
		# 		for agg_flag in ['CV-splits-nit-10']: #'CV-splits-nit-10', 'best_voxelwise', 'LOSO'
		# 			for randnetw_flag in ['True']: # 'False', 'True'
		# 				barplot_across_models(source_models, target=target, roi=None, df_meta_roi=df_meta_roi,
		# 									  save=SAVEDIR_CENTRALIZED, randnetw=randnetw_flag,
		# 									  aggregation=agg_flag, value_of_interest=val_flag,
		# 									  sort_by=sort_flag,
		# 									  add_savestr=f'_{datetag}')
		#
		# # STATS FOR BARPLOTS ACROSS MODELS (bootstrap across subjects)
		# for val_flag in ['median_r2_test_c', 'median_r2_test']:
		# 	for randnetw_flag in ['False','True']:
		# 		compare_models_subject_bootstrap(source_models=source_models, target=target, df_meta_roi=df_meta_roi,
		# 										 save=True, value_of_interest=val_flag,
		# 							  save_str='all-models_subject-bootstrap',
		# 							  models1=[ 'ResNet50multitask',],
		# 							  models2=['Kell2018word', 'Kell2018speaker',  'Kell2018music', 'Kell2018audioset', 'Kell2018multitask',
		# 		 							'ResNet50word', 'ResNet50speaker', 'ResNet50music', 'ResNet50audioset',   'ResNet50multitask',
		# 										],
		# 							  aggregation='CV-splits-nit-10',
		# 							  randnetw=randnetw_flag, )
		
		# STATS FOR BARPLOTS ACROSS MODELS (if using iteration splits AND subjects)
		# compare_CV_splits_nit(source_models=source_models, target=target, save=True, value_of_interest='median_r2_test_c',
		# 					  save_str='inhouse-models_CochCNN9-bootstrapTEST',
		# 					  models1=['Kell2018word', 'Kell2018speaker',  'Kell2018music', 'Kell2018audioset', 'Kell2018multitask',
		# 		 'ResNet50word', 'ResNet50speaker', 'ResNet50music', 'ResNet50audioset',   'ResNet50multitask',
		# 		'AST',  'wav2vec', 'DCASE2020', 'DS2', 'VGGish',  'ZeroSpeech2020', 'S2T', 'metricGAN', 'sepformer'],
		# 					  models2=['Kell2018word', 'Kell2018speaker',  'Kell2018music', 'Kell2018audioset', 'Kell2018multitask',
		# 		 'ResNet50word', 'ResNet50speaker', 'ResNet50music', 'ResNet50audioset',   'ResNet50multitask',
		# 		'AST',  'wav2vec', 'DCASE2020', 'DS2', 'VGGish',  'ZeroSpeech2020', 'S2T', 'metricGAN', 'sepformer'],
		# 					  aggregation='CV-splits-nit-10',
		# 					  randnetw='False', )
		# #
		# # # ANATOMICAL SCATTER PLOTS
		save_str = '_good-models'
		for val_flag in ['median_r2_test_c', 'median_r2_test']: # 'median_r2_test_c', 'median_r2_test'
			for non_primary_flag in ['Anterior', 'Lateral', 'Posterior']:
				for cond_flag in ['roi_label_general']:
					for collapse_flag in ['median', 'mean']: # 'median', 'mean'
						for randnetw_flag in ['True']: # 'True', 'False'
							scatter_anat_roi_across_models(source_models, target=target, save=SAVEDIR_CENTRALIZED, randnetw=randnetw_flag,
														   condition_col=cond_flag, collapse_over_val_layer=collapse_flag,
														   primary_rois=['Primary'],
														   non_primary_rois=[non_primary_flag], annotate=False, save_str=save_str,
														   value_of_interest=val_flag,
														   layers_to_exclude=['input_after_preproc'])
	
		# # ANATOMICAL SCATTER PLOTS: dim analyses
		# save_str = '_inhouse-models_dim'
		# for val_flag in ['median_r2_test_c']:
		# 	for non_primary_flag in ['Anterior', 'Lateral', 'Posterior']:
		# 		for cond_flag in ['roi_label_general']:
		# 			for collapse_flag in ['median',]:
		#
		# 				# TRAINED NETWORK
		# 				scatter_anat_roi_across_models(source_models, target=target, save=SAVEDIR_CENTRALIZED, randnetw='False',
		# 											   condition_col=cond_flag, collapse_over_val_layer=collapse_flag,
		# 											   primary_rois=['Primary'],
		# 											   non_primary_rois=[non_primary_flag], annotate=False, save_str=save_str,
		# 											   value_of_interest=val_flag, layer_value_of_interest='dim_demean-True')
		#
		# 				# RANDOM NETWORK
		# 				scatter_anat_roi_across_models(source_models, target=target, save=SAVEDIR_CENTRALIZED, randnetw='True',
		# 											   condition_col=cond_flag, collapse_over_val_layer=collapse_flag,
		# 											   primary_rois=['Primary'],
		# 											   non_primary_rois=[non_primary_flag], annotate=False,
		# 											   save_str=save_str,
		# 											   value_of_interest=val_flag,
		# 											   layer_value_of_interest='dim_randnetw_demean-True')
					
	
	
		
		## LOAD SCORE ACROSS LAYERS (FOR DIMENSIONALITY ANALYSIS -- migrated to DIM_plot_main)
		# load_score_across_layers_across_models(source_models=source_models,
		# 									   RESULTDIR_ROOT=RESULTDIR_ROOT,)
					
		# DETERMINE COLOR SCALE FOR SURFACE MAPS (also copied over to target = NH2015-B2021, but leaving here for now)
		# if len(source_models) == 19: # All
		# 	for randnetw_flag in ['False', 'True']:
		# 		determine_surf_layer_colorscale(target='NH2015-B2021', source_models=source_models, randnetw=randnetw_flag,
		# 										save=PLOTSURFDIR)
		#
		# # Create median surface across models
		# if len(source_models) == 15: # good models!
		# 	for val_flag in ['median_r2_test_c', 'median_r2_test']:
		# 		for randnetw_flag in ['False','True']:
		# 			df_median_model_surf = create_avg_model_surface(source_models, target, PLOTSURFDIR,
		# 															val_of_interest=val_flag, randnetw=randnetw_flag,
		# 															plot_val_of_interest='rel_pos',
		# 															quantize=False)
		# 			df_median_model_surf_quantized = create_avg_model_surface(source_models, target, PLOTSURFDIR,
		# 															  val_of_interest=val_flag, randnetw=randnetw_flag,
		# 															  plot_val_of_interest='rel_pos',
		# 															  quantize=True)
		# 			dump_for_surface_writing_avg(df_median_model_surf, source_model='all-good-models', SURFDIR=SURFDIR,
		# 										 randnetw=randnetw_flag, subfolder_name=f'TYPE=subj-median-argmax-model-median_METRIC={val_flag}_PLOTVAL=rel_pos*10+1'
		# 																		f'_{target}' )
		# 			dump_for_surface_writing_avg(df_median_model_surf_quantized, source_model='all-good-models', SURFDIR=SURFDIR,
		# 										 randnetw=randnetw_flag, subfolder_name=f'TYPE=subj-median-argmax-model-median_METRIC={val_flag}_PLOTVAL=rel_pos*10+1-quantized'
		# 																		f'_{target}' )
	
		else:
			print(f'Target ({target}) not recognized')


if not concat_over_models:
	for source_model in source_models:
		print(f'\n######### MODEL: {source_model} ##########\n')
		#### Identifier information #####
		randemb = 'False'
		mapping = 'AUD-MAPPING-Ridge'
		alpha_str = '50'
		
		#### Paths (source model specific) ####
		RESULTDIR = (Path(f'{ROOT}/results/AUD/20210915_median_across_splits_correction/{source_model}')).resolve()
		DIAGDIR = (Path(join(RESULTDIR, f'diagnostics_TARGET-{target}_RANDNETW-{randnetw}_ALPHALIMIT-{alpha_str}')))
		PLOTDIR = (Path(f'{ROOT}/results/AUD/20210915_median_across_splits_correction/{source_model}/outputs')).resolve()
		PLOTDIR.mkdir(exist_ok=True)
		
		# Load voxel meta
		df_meta_roi = pd.read_pickle(join(DATADIR, 'neural', target, 'df_roi_meta.pkl'))
		meta = df_meta_roi.copy(deep=True) # for adding plotting values
		
		# spectemp_path = [f'{ROOT}/results/AUD/20210915_median_across_splits_correction/spectemp/AUD-MAPPING-Ridge_TARGET-B2021_SOURCE-spectemp-avgpool_RANDEMB-False_RANDNETW-False_ALPHALIMIT-50']
		# concat_ds_B2021(source_model='spectemp', output_folders_paths=spectemp_path,
		# 				df_roi_meta=df_meta_roi, randnetw=randnetw)

		# Load output results
		output, output_folders = concat_dfs_modelwise(RESULTDIR, mapping=mapping, df_str='df_output', source_model=source_model, target=target,
													  truncate=None, randemb=randemb, randnetw=randnetw)
		output_folders_paths = [join(RESULTDIR, x) for x in output_folders]
		
		# Concatenate ds for B2021 (IF NOT DONE YET)
		# concat_ds_B2021(source_model=source_model, output_folders_paths=output_folders_paths,
		# 				df_roi_meta=df_meta_roi, randnetw=randnetw)
		# assert_output_ds_match(output_folders_paths=output_folders_paths)
		
		if source_model == 'wav2vec':  # rename 'Logits' to Final
			output.loc[output.source_layer == 'Logits', 'source_layer'] = 'Final'
		
		# Ensure that r2 test corrected does exceed 1
		output['median_r2_test_c'] = output['median_r2_test_c'].clip(upper=1)
		output['mean_r2_test_c'] = output['mean_r2_test_c'].clip(upper=1)
		
		######### ROI/VOXEL ANALYSES - WITHIN-SUBJECT ERROR ########
		if run_agg:
			#### LOAD DATA ####
			if source_model.endswith('init') or source_model == 'spectemp' or source_model == 'wav2vecpower':
				plot_score_across_layers(output, source_model=source_model, target=target, ylim=[0, 1], roi=None,
										 save=PLOTDIR, output_randnetw=None, value_of_interest='median_r2_test_c',
										 )

			else:
				if randnetw != 'True':  # otherwise it just reloads..
					# Get corresponding random network
					output_randnetw, output_folders_randnetw = concat_dfs_modelwise(RESULTDIR, mapping=mapping, df_str='df_output',
															  source_model=source_model,
															  target=target, truncate=None, randemb=randemb,
															  randnetw='True')
					output_randnetw['median_r2_test_c'] = output_randnetw['median_r2_test_c'].clip(upper=1)
					output_randnetw['mean_r2_test_c'] = output_randnetw['mean_r2_test_c'].clip(upper=1)
					output_folders_paths_randnetw = [join(RESULTDIR, x) for x in output_folders_randnetw]


			if target == 'NH2015comp':  # components
				# for randnetw_flag in ['False']:
				# 	if randnetw_flag == 'True':
				# 		select_r2_test_CV_splits_nit(output_folders_paths=output_folders_paths_randnetw, df_meta_roi=df_meta_roi, source_model=source_model,
				# 								 target=target, value_of_interest='r2_test', randnetw=randnetw_flag, save=PLOTDIR)
				# 	elif randnetw_flag == 'False':
				# 		select_r2_test_CV_splits_nit(output_folders_paths=output_folders_paths, df_meta_roi=df_meta_roi, source_model=source_model,
				# 								 target=target, value_of_interest='r2_test', randnetw=randnetw_flag, save=PLOTDIR)
				# 	else:
				# 		raise ValueError()
				
				
				# # Plot components across layers, and store 'across-layers_{source_model}_NH2015comp_{value_of_intereset}.csv'
				plot_comp_across_layers(output=output, source_model=source_model, output_randnetw=output_randnetw,
										target=target, save=PLOTDIR, value_of_interest='median_r2_test')
				plot_comp_across_layers(output=output, source_model=source_model, output_randnetw=output_randnetw,
										target=target, save=PLOTDIR, value_of_interest='median_r2_train')
				#
				# # Per component, find the best layer and obtain the associated r2 test score (stores the 'best-layer-argmax_per-comp_{source_model}_NH2015comp_{value_of_interest}.csv')
				# # Trained and permuted:
				# for randnetw_flag in ['False','True']:
				# 	obtain_best_layer_per_comp(source_model=source_model, target=target, randnetw=randnetw_flag,
				# 							   value_of_interest='median_r2_test', sem_of_interest='sem_r2_test', )
				# 	obtain_best_layer_per_comp(source_model=source_model, target=target, randnetw=randnetw_flag,
				# 							   value_of_interest='median_r2_train', sem_of_interest='sem_r2_train', )
				#
				# # Per component, select the best layer based on r2 train and get the r2 test value for that layer
				# # (stores the f'best-layer-CV-splits-train-test_per-comp_{source_model}_NH2015_{value_of_interest}.csv')
				# # Also use this info to denote which scatterplot (resp vs pred) layer is used.
				# for randnetw_flag in ['False','True']:
				# 	select_r2_test_CV_splits_train_test(source_model=source_model, target=target, randnetw=randnetw_flag, )
			

			else:  # Neural data
				if target != 'B2021':  # target = NH2015
					roi_flags = [None, 'any_roi', 'all']  # Functional ROIs available
				elif target == 'B2021':  # target = B2021
					roi_flags = [None]  # No functional ROIs available
				else:
					raise ValueError('Target not available')

				# Best layer based on CV splits -- TRAINED and PERMUTED NETWORK, loop over collapsing either 'median' or 'mean'
				# for collapse_flag in ['median']:
				# 	for val_flag in ['r2_test', 'r2_test_c']: #
				# 		for randnetw_flag in ['False', 'True']:  #
				# 			if randnetw_flag == 'True':  # replace the RANDNETW-False with True in the output folders paths
				# 				select_r2_test_CV_splits_nit(output_folders_paths_randnetw, df_meta_roi=df_meta_roi,
				# 											 collapse_over_splits=collapse_flag,
				# 											 source_model=source_model, target=target,
				# 											 value_of_interest=val_flag,
				# 											 randnetw='True', roi=None, save=PLOTDIR, nit=10)
				# 			elif randnetw_flag == 'False':
				# 				select_r2_test_CV_splits_nit(output_folders_paths, df_meta_roi=df_meta_roi,
				# 											 collapse_over_splits=collapse_flag,
				# 											 source_model=source_model, target=target,
				# 											 value_of_interest=val_flag,
				# 											 randnetw=randnetw_flag, roi=None, save=PLOTDIR, nit=10)
				# 			else:
				# 				raise ValueError()
				# 		sys.stdout.flush()

				# # # Best layer voxelwise -- TRAINED and PERMUTED NETWORK
				# for val_flag in ['median_r2_test', 'median_r2_test_c']: #'median_r2_test', 'median_r2_test_c'
				# 	for randnetw_flag in ['False', 'True']:
				# 		if randnetw_flag == 'True':
				# 			best_layer_voxelwise(output_randnetw, source_model=source_model, target=target,
				# 								 df_meta_roi=df_meta_roi,
				# 								 value_of_interest=val_flag, randnetw=randnetw_flag, roi=None,
				# 								 save=PLOTDIR)
				# 		elif randnetw_flag == 'False':
				# 			best_layer_voxelwise(output, source_model=source_model, target=target,
				# 								 df_meta_roi=df_meta_roi,
				# 								 value_of_interest=val_flag, randnetw=randnetw_flag, roi=None,
				# 								 save=PLOTDIR)
				# 		else:
				# 			raise ValueError()
				# 	sys.stdout.flush()
				#
				# # Barplots (and obtain LOSO values for across-models plot) -- TRAINED and PERMUTED NETWORK
				# for roi_flag in roi_flags:
				# 	for val_flag in ['median_r2_test', 'median_r2_test_c']:
				# 		for randnetw_flag in ['False', 'True']:
				# 			if randnetw_flag == 'True':
				# 				plot_LOSO_best_layer_bars(output_randnetw, source_model=source_model, target=target, roi=roi_flag,
				# 										  save=PLOTDIR, randnetw=randnetw_flag, value_of_interest=val_flag)
				# 			elif randnetw_flag == 'False':
				# 				plot_LOSO_best_layer_bars(output, source_model=source_model, target=target, roi=roi_flag,
				# 										  save=PLOTDIR, randnetw=randnetw_flag, value_of_interest=val_flag)
				# 			else:
				# 				raise ValueError()
				# 			sys.stdout.flush()
				#
				# # # # Barplots of best layer for anatomical ROIs -- TRAINED and PERMUTED NETWORK
				for cond_flag in ['roi_label_general']: # ['roi_label_general','roi_anat_hemi' ]
					for collapse_flag in ['median', 'mean']: # ['median', 'mean'] # which aggfunc to use when obtaining an aggregate over rel_pos layer index values for each subject
						for val_flag in ['median_r2_test', 'median_r2_test_c',]: # ['median_r2_test', 'median_r2_test_c',]
							for randnetw_flag in ['True']: # ['False', 'True',]

									if randnetw_flag == 'True':
										if source_model.startswith('Kell2018') or source_model.startswith('ResNet50'):
											layers_to_exclude = ['input_after_preproc']
										else:
											layers_to_exclude = None
											
										barplot_best_layer_per_anat_ROI(output_randnetw, meta, source_model=source_model,
																		target=target,
																		randnetw=randnetw_flag, collapse_over_val_layer=collapse_flag,
																		save=PLOTDIR, condition_col=cond_flag, value_of_interest=val_flag,
																		val_layer='rel_pos',
																		layers_to_exclude=layers_to_exclude)
									elif randnetw_flag == 'False':
										barplot_best_layer_per_anat_ROI(output, meta, source_model=source_model, target=target,
																		randnetw=randnetw_flag, collapse_over_val_layer=collapse_flag,
																		save=False, condition_col=cond_flag, value_of_interest=val_flag,
																		val_layer='rel_pos',
																		layers_to_exclude=None) # PLOTDIR to save!
									else:
										raise ValueError()
				
				# # # # Barplots of best layer for anatomical ROIs -- TRAINED and PERMUTED NETWORK: dimensionality values! (same func as for neural)
				# for cond_flag in ['roi_label_general']: # ['roi_label_general','roi_anat_hemi' ]
				# 	for collapse_flag in ['median']: # ['median', 'mean'] # which aggfunc to use when obtaining an aggregate over rel_pos layer index values for each subject
				# 		for val_flag in ['median_r2_test_c',]: # ['median_r2_test', 'median_r2_test_c',]
				# 			for randnetw_flag in ['False', 'True']: # ['False', 'True',]
				#
				# 					if randnetw_flag == 'True':
				# 						barplot_best_layer_per_anat_ROI(output_randnetw, meta, source_model=source_model,
				# 														target=target,
				# 														randnetw=randnetw_flag, collapse_over_val_layer=collapse_flag,
				# 														save=PLOTDIR, condition_col=cond_flag, value_of_interest=val_flag,
				# 														val_layer='dim_randnetw_demean-True')
				# 					elif randnetw_flag == 'False':
				# 						barplot_best_layer_per_anat_ROI(output, meta, source_model=source_model, target=target,
				# 														randnetw=randnetw_flag, collapse_over_val_layer=collapse_flag,
				# 														save=PLOTDIR, condition_col=cond_flag, value_of_interest=val_flag,
				# 														val_layer='dim_demean-True')
				# 					else:
				# 						raise ValueError()
				#
									sys.stdout.flush()
				#
				# # R2 across layers -- automatically adds randnetw if loaded
				# for roi_flag in roi_flags:
				# 	for val_flag in ['median_r2_test_c', 'median_r2_test', ]:
				# 		plot_score_across_layers(output, source_model=source_model, target=target, ylim=[0, 1],
				# 								 roi=roi_flag,
				# 								 save=PLOTDIR, output_randnetw=output_randnetw,
				# 								 value_of_interest=val_flag)
				#
				# if plot_subjectwise:
				# 	for subj_idx in (
				# 	output.subj_idx.unique()):  # If running for B2021, was previously for subj_idx in np.arange(1,21): (check if same as output.subj_idx.unique())
				# 		plot_score_across_layers_per_subject(output, source_model=source_model, subj_idx_lst=[subj_idx],
				# 											 target=target, ylim=[0, 1], roi=None, save=PLOTDIR,
				# 											 output_randnetw=output_randnetw,
				# 											 value_of_interest='median_r2_test_c')
				#
		######### SURFACE ANALYSES ########
		if run_surf:  # surf has to be run with randnetw False and True separately
			PLOTSURFDIR.mkdir(exist_ok=True)
			save_full_surface = True
			
			##### Generate plots by plotting certain values of interest directly on the surface #####
			val_flags = ['kell_r_reliability', 'roi_label_general', 'pearson_r_reliability', 'shared_by']
			
			# Transform values
			for val_flag in val_flags:
				# Transformations
				if val_flag.endswith('reliability'):
					val_flag_to_plot = f'{val_flag}*10'
				elif val_flag == 'roi_label_general':
					val_flag_to_plot = 'roi_label_general_int'
				else:
					val_flag_to_plot = val_flag
					
				df_plot_direct = direct_plot_val_surface(output=output,
														 df_meta_roi=df_meta_roi,
														 val=val_flag,)
				
				# Make sure we take the median across shared coordinates across subjects!
				df_plot_direct_median = create_avg_subject_surface(df_plot=df_plot_direct,
																   source_model=source_model,
																   val_of_interest=val_flag_to_plot, # does not really matter here besides for logging..
																   meta=meta,
																   save=PLOTSURFDIR,
																   target=target,
																   randnetw=randnetw,
																   plot_val_of_interest=val_flag_to_plot,
																   save_full_surface=True)
				
				# Dump to mat file
				dump_for_surface_writing_direct(df_plot_direct=df_plot_direct_median,
												val='median_plot_val',#val_flag_to_plot,
												 source_model=source_model,
												 SURFDIR=SURFDIR,
												 randnetw=randnetw,
												 subfolder_name=f'TYPE=subj-median-direct_PLOTVAL={val_flag_to_plot}_{target}')
			
			######## Surface argmax plots #########
			for val_flag in ['median_r2_test_c', 'median_r2_test']:
				for plot_val_flag in ['pos', 'rel_pos']:
					
					## SUBJECT-WISE ARGMAX ANALYSIS ##
					df_plot, layer_names = surface_argmax(output, source_model=source_model, target=target, randnetw=randnetw,
														  value_of_interest=val_flag, hist=True, save=PLOTSURFDIR)
					
					# Dump subject-wise mat files
					dump_for_surface_writing(vals=df_plot[plot_val_flag],
											 meta=meta,
											 source_model=source_model,
											 SURFDIR=False,  # SURFDIR
											 randnetw=randnetw,
											 subfolder_name=f'TYPE=subj-argmax_METRIC={val_flag}_PLOTVAL={plot_val_flag}_'
															f'{target}')
					
					## AVERAGE SUBJECT ##
					if merge_surface_targets:  # load the other target dataset
						# Load output results
						output2, _ = concat_dfs_modelwise(RESULTDIR, mapping=mapping, df_str='df_output',
														  source_model=source_model, target=d_target[target],
														  truncate=None, randemb=randemb, randnetw=randnetw)
						# Load meta
						df_meta_roi2 = pd.read_pickle(join(DATADIR, 'neural', d_target[target], 'df_roi_meta.pkl'))
						meta2 = df_meta_roi2.copy(deep=True)  # for adding plotting values
						meta2['target'] = d_target[target]
						
						if source_model == 'wav2vec':  # rename 'Logits' to Final
							output2.loc[output2.source_layer == 'Logits', 'source_layer'] = 'Final'
						
						# Ensure that r2 test corrected does exceed 1
						output2['median_r2_test_c'] = output2['median_r2_test_c'].clip(upper=1)
						
						df_plot2, layer_names2 = surface_argmax(output2, source_model=source_model, target=d_target[target],
																randnetw=randnetw, value_of_interest=val_flag, hist=True,
																save=PLOTSURFDIR)
						
						# Also save subjwise files for target 2
						dump_for_surface_writing(df_plot2[plot_val_flag], meta2, source_model, SURFDIR, randnetw=randnetw,
												 subfolder_name=f'TYPE=subj-argmax_METRIC={val_flag}_PLOTVAL={plot_val_flag}_'
																f'{d_target[target]}')
						
						# Store median subject surface map for secondary dataset
						median_subj2 = create_avg_subject_surface(df_plot=df_plot2, meta=meta2, source_model=source_model, save=PLOTSURFDIR,
																  target=d_target[target], val_of_interest=val_flag,
																  plot_val_of_interest=plot_val_flag, randnetw=randnetw, save_full_surface=True)
						dump_for_surface_writing_avg(median_subj2, source_model, SURFDIR, randnetw=randnetw,
													 subfolder_name=f'TYPE=subj-median-argmax_METRIC={val_flag}_PLOTVAL={plot_val_flag}_'
																	f'{d_target[target]}')
						
						assert (layer_names == layer_names2).all()
						
						# Median subj, based on both datasets
						meta['target'] = target
						median_subj = create_avg_subject_surface_merge_targets(df_plot1=df_plot, meta1=meta,
																			   df_plot2=df_plot2, meta2=meta2, plot_val_of_interest=plot_val_flag)
						
						# Plot histogram for layer preference across voxels from both datasets
						surface_argmax_hist_merge_datasets(df_plot1=df_plot, df_plot2=df_plot2, source_model=source_model,
														   save=PLOTSURFDIR, randnetw=randnetw, layer_names=layer_names)
						
						# Dump the average (median across subjects) brain to the surface
						dump_for_surface_writing_avg(median_subj, source_model, SURFDIR, randnetw=randnetw,
													 subfolder_name=f'TYPE=subj-median-argmax_METRIC={val_flag}_PLOTVAL={plot_val_flag}'
																	f'_{target}-{d_target[target]}')
					
					# Just use the first output to create the surface for primary target (independent of whether I am merging or not)
					median_subj1 = create_avg_subject_surface(df_plot=df_plot, meta=meta, source_model=source_model, save=PLOTSURFDIR,
																  target=target, val_of_interest=val_flag,
																  plot_val_of_interest=plot_val_flag, randnetw=randnetw, save_full_surface=True)
					
					# Dump the average (median across subjects) brain to the surface
					dump_for_surface_writing_avg(median_subj1, source_model, SURFDIR, randnetw=randnetw,
												 subfolder_name=f'TYPE=subj-median-argmax_METRIC={val_flag}_PLOTVAL={plot_val_flag}'
																f'_{target}')
					
					sys.stdout.flush()
		
		
		
		
		
		######### DIAGNOSTIC ANALYSES ########
		if run_diag:
			DIAGDIR.mkdir(exist_ok=True)
			
			if target == 'NH2015comp':
				loop_through_comp_diagnostics(output_folders_paths, DIAGDIR=DIAGDIR, source_model=source_model, target=target, randnetw=randnetw)
				
				# Aggregate and plot
				# Related to visualizing warnings
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='warning_constant_mean_PERC',ylim=[0, 50], save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='warning_alphas_upper_PERC', ylim=[0, 50], save=True)
				
				# Related to negative r test
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='neg_r_test_PERC', ylim=[0, 50],save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='neg_r_test_MEDIAN', ylim=[-10, 0],save=True)
				
				# Related to NaNs
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='nan_r_prior_zero_PERC', ylim=[0, 50],save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='nan_r2_train_PERC', ylim=[0, 50],save=True)
			
				
				# Comparative, e.g. what was a given value for problematic versus nonproblematic voxels/splits
				plot_two_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target,
									 val_of_interest1='r_prior_zero_constant_warning_mean_MEDIAN',
									 val_of_interest2='r_prior_zero_no_constant_warning_mean_MEDIAN', ymax=None,save=True)
				plot_two_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target,
									 val_of_interest1='r2_train_constant_warning_mean_MEDIAN',
									 val_of_interest2='r2_train_no_constant_warning_mean_MEDIAN', ymax=None, save=True)
				plot_two_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target,
									 val_of_interest1='alphas_constant_warning_mean_MEDIAN',
									 val_of_interest2='alphas_no_constant_warning_mean_MEDIAN', ymax=None, save=True)
			
			elif target == 'B2021':
				loop_through_chunked_diagnostics(output_folders_paths, DIAGDIR=DIAGDIR, source_model=source_model, target=target, randnetw=randnetw)
				
				for chunk_i in range(4):
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='warning_constant_mean_PERC', ylim=[0, 50], save=True)
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='warning_constant_splits_PERC', ylim=[0, 50], save=True)
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='warning_alphas_upper_PERC', ylim=[0, 50], save=True)
					
					# Related to negative r test
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='neg_r_test_PERC', ylim=[0, 50], save=True)
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='neg_r_test_MEDIAN', ylim=[-10, 0], save=True)
					
					# Related to NaNs
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='nan_r_prior_zero_PERC', ylim=[0, 50], save=True)
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='nan_r2_train_PERC', ylim=[0, 50], save=True)
					
					# Related to r2 corrected values exceeding 1
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='exceed1_r2_test_c_PERC', ylim=[0, 50], save=True)
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='exceed1_r2_test_c_MAX', ylim=[0, 20], save=True)
					plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=f'{target}_chunk-{chunk_i}',
									 val_of_interest='exceed1_r2_test_c_MEDIAN', ylim=[0, 10], save=True)
					
					# look into voxels where the r2 corrected exceeds 1
					r2_corrected_exceed1(output, source_model=source_model, target=target, save=DIAGDIR)
					
			else:
				loop_through_diagnostics(output_folders_paths, DIAGDIR=DIAGDIR, source_model=source_model, target=target, randnetw=randnetw)

				# Check CV boundary by using log files
				problematic_vox = check_alpha_ceiling(output_folders_paths, DIAGDIR=DIAGDIR, source_model=source_model,
													  target=target, randnetw=randnetw, save=True)
				# Plot alpha versus reliability
				reliability_vs_alpharange(df_meta_roi, problematic_vox=problematic_vox, source_model=source_model,
										  target=target, randnetw=randnetw, save=DIAGDIR)

				# Aggregate and plot
				# Related to visualizing warnings
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='warning_constant_mean_PERC', ylim=[0,50], save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='warning_constant_splits_PERC', ylim=[0,50], save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='warning_alphas_upper_PERC', ylim=[0,50], save=True)

				# Related to negative r test
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='neg_r_test_PERC', ylim=[0,50], save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='neg_r_test_MEDIAN', ylim=[-10,0], save=True)

				# Related to NaNs
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='nan_r_prior_zero_PERC', ylim=[0,50], save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='nan_r2_train_PERC', ylim=[0,50], save=True)

				# Related to r2 corrected values exceeding 1
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='exceed1_r2_test_c_PERC', ylim=[0,50], save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='exceed1_r2_test_c_MAX', ylim=[0,20], save=True)
				plot_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest='exceed1_r2_test_c_MEDIAN', ylim=[0,10], save=True)


				# Comparative, e.g. what was a given value for problematic versus nonproblematic voxels/splits
				plot_two_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest1='r_prior_zero_constant_warning_mean_MEDIAN',
									 val_of_interest2='r_prior_zero_no_constant_warning_mean_MEDIAN', ymax=None, save=True)
				plot_two_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest1='r2_test_c_constant_warning_mean_MEDIAN',
									 val_of_interest2='r2_test_c_no_constant_warning_mean_MEDIAN', ymax=None, save=True)
				plot_two_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest1='r2_train_constant_warning_mean_MEDIAN',
									 val_of_interest2='r2_train_no_constant_warning_mean_MEDIAN', ymax=None, save=True)
				plot_two_diagnostics(DIAGDIR, source_model=source_model, randnetw=randnetw, target=target, val_of_interest1='alphas_constant_warning_mean_MEDIAN',
									 val_of_interest2='alphas_no_constant_warning_mean_MEDIAN', ymax=None, save=True)

				# look into voxels where the r2 corrected exceeds 1
				r2_corrected_exceed1(output, source_model=source_model, target=target, save=DIAGDIR)

		

			
		if do_stats:
			
			def null_distribution_ind_vox(num_splits=10, num_it=1000):
				"""
				Generate a null distribution for individual voxel predictions, from Kell et al., 2018 methods:
				
				
				"""
				# Check significance of individual voxel predictions
				mock_corr_medians = []
				for it in range(num_it):
					mock_corrs = []
					for split in range(num_splits):
						v1 = np.random.normal(size=82, loc=0, scale=1)
						v2 = np.random.normal(size=82, loc=0, scale=1)
						
						mock_corr = np.corrcoef(v1, v2)[1,0]
						mock_corrs.append(mock_corr)
				
					mock_corr_median = np.median(mock_corrs)
					mock_corr_medians.append(mock_corr_median)
		
	
			
			
			
	
		
	
