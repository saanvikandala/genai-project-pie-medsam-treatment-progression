# genai-project-pie-medsam-treatment-progression
Gen AI Project: PIE-MedSAM: Simulating Disease Treatment Progression Via Progressive Image Editing And ROI-Aware Feedback

Summary:
-
- The project adapts the work done in the PIE: Simulating Disease Progression via Progressive Image Editing paper to fine-tune PIE for generating image-level progressive images to simulate treatment progression in glioblastoma tumor MRI scans. Experiments include integrating medical-domain based segmentation masks generated using MedSAM instead of the SAM masks used in the original paper. Two experiments are conducted by varying the bounding box: 1) bounding box for full image (full-boxing) 2) auto-generated bounding box around the largest "blob" (auto-boxing).

Findings include: 
-
- Comparable results between fine-tuned treatment progression baseline model to original PIE disease model from original paper
- Comparable results between baseline model and experiments with MedSAM integrated masks
- Full-boxing: Higher CLIP-I score -> Better structure preservation in progressed images
- Auto-boxing: Higher classification confidence score -> More successful tumor-related edits over progressed images  
