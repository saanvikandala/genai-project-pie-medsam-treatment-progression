# genai-project-pie-medsam-treatment-progression
Gen AI Project: PIE-MedSAM: Simulating Disease Treatment Progression Via Progressive Image Editing And ROI-Aware Feedback

Our project adapts the work done in the PIE: Simulating Disease Progression via Progressive Image Editing paper to fine-tune PIE for generating image-level progressive images to simulate treatment progression in glioblastoma tumor MRI scans. We then experiment with integrating medical-domain based segmentation masks generated using MedSAM instead of the SAM masks used in the original paper. We conduct two experiments by varying the bounding box: 1) bounding box for full image (full-boxing) 2) auto-generated bounding box around the largest "blob" (auto-boxing).
